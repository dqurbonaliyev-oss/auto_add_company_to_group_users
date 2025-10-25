# Automatic Company Access Assignment

Automatically assign newly created companies to users who belong to specific groups.

## 🧩 Overview

This module ensures that when a new company is created in Odoo, it is automatically added to the _Allowed Companies_ (
`allowed_company_ids`) list of users that belong to the configured groups.

This helps administrators avoid manually updating company access rights for multiple users each time a new company is
created.

## ⚙️ Configuration

You can configure which groups this automation applies to using the System Parameters menu in Odoo.

1. Go to **Settings → Technical → Parameters → System Parameters**
   (Make sure Developer Mode is activated.)
2. Click **Create** (or **Edit** if it already exists).
3. Fill in the fields as follows:
    - Key: `auto_add_company.group_xml_ids`
    - Value: Comma-separated list of group external IDs, e.g.

```text
base.group_system,base.group_user
```

4. Click **Save**.

That’s it! From now on, any new company created in the system will automatically be added to the **Allowed Companies**
list of users who belong to the specified groups.