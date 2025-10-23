from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

CONFIG_PARAM_KEY = 'auto_add_company.group_xml_ids'  # comma-separated external XML ids of groups


class ResCompany(models.Model):
    _inherit = 'res.company'

    @api.model_create_multi
    def create(self, vals_list):
        """
        Handle multi-create: create companies, then add each created company
        to allowed_company_ids of users belonging to configured groups.
        """
        # create companies first
        companies = super(ResCompany, self).create(vals_list)

        try:
            param = self.env['ir.config_parameter'].sudo().get_param(CONFIG_PARAM_KEY, default='')
            if not param:
                _logger.debug('auto_add_company: no groups configured in %s', CONFIG_PARAM_KEY)
                return companies

            xml_ids = [x.strip() for x in param.split(',') if x.strip()]
            groups = self.env['res.groups'].browse()
            for xml in xml_ids:
                try:
                    group = self.env.ref(xml, raise_if_not_found=False)
                    if group:
                        groups |= group
                    else:
                        _logger.warning('auto_add_company: group XML id not found: %s', xml)
                except Exception:
                    _logger.exception('auto_add_company: error resolving xml id %s', xml)

            if not groups:
                _logger.debug('auto_add_company: no valid groups resolved from %s', CONFIG_PARAM_KEY)
                return companies

            users = groups.mapped('users')
            if not users:
                _logger.debug('auto_add_company: resolved groups have no users')
                return companies

            # Prepare (4, id) commands for all created companies
            company_commands = [(4, comp.id) for comp in companies]
            # Use sudo() to ensure we can update allowed_company_ids even if current user lacks permission
            users.sudo().write({'company_ids': company_commands})
            _logger.info('auto_add_company: added %s new companies to %s users', len(companies), len(users))
        except Exception:
            _logger.exception('auto_add_company: unexpected error while adding companies to users')

        return companies
