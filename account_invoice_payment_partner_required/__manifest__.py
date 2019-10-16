# Copyright 2019 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Account Invoice Payment Mode Mandatory',
    'version': '11.0.1.0.0',
    'summary': """Makes the Payment Mode and Payment Terms fields of the
               invoice mandatory.""",
    'author': 'Daniel Luque',
    'website': "https://github.com/LuqueDaniel/odoo-custom-addons",
    'license': 'AGPL-3',
    'category': 'Banking addons',
    'depends': ['account_payment_partner'],
    'data': [
        'views/account_invoice_view.xml'
    ],
    'installable': True
}
