{
    'name': 'Automatic Company Access Assignment',
    'version': '18.0.1.0.0',
    'summary': 'Automatically assigns newly created companies to users in specific groups.',
    'description': """
                                              This module ensures that when a new company is created, it is automatically added 
                                              to the *Allowed Companies* list (`allowed_company_ids`) of users who belong to 
                                              the groups configured in system parameters.
                                          """,
    'author': 'UIC Group',
    'contributors': [
        'Asliddin Maxmudov'
    ],
    'website': 'https://uic.group/',
    'license': 'LGPL-3',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'data/ir_config_parameter.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
