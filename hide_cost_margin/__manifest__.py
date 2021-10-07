# Copyright 2017-2018 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "Hide costs and margins",
    "version": "12.0.1.0.3",
    "summary": "Hides the costs and margins fields of some views",
    "author": "Daniel Luque",
    "website": "https://github.com/LuqueDaniel/odoo-custom-addons",
    "license": "AGPL-3",
    "category": "Sales",
    "depends": ["sale_margin"],
    "data": ["security/groups.xml", "views/sale.xml"],
    "installable": True,
}
