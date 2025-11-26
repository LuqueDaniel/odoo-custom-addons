# Copyright 2019 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "Permission to Cancel Journal Entries",
    "version": "13.0.1.0.0",
    "summary": "Only shows the button to cancel invoices, payments and "
    "bank statements to users with 'Cancel Journal Entries' "
    "permission",
    "author": "Daniel Luque",
    "website": "https://github.com/LuqueDaniel/odoo-custom-addons",
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": ["account"],
    "data": ["security/groups.xml", "views/account_cancel.xml"],
    "application": False,
    "auto_install": False,
    "installable": True,
}
