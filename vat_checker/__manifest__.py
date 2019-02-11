# -*- coding: utf-8 -*-
# Copyright 2017-2018 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Check VAT number before create invoice',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'summary': 'Check if the customer has a VAT before creating an invoice',
    'description': """
        Check if the customer has a VAT before creating an invoice from a
        sale order.
        """,
    'author': 'Daniel Luque',
    'website': 'https://github.com/LuqueDaniel/odoo_custom_addons',
    'category': 'Invoicing & Payments',
    'depends': ['sale', 'base_vat'],
    'installable': True
}
