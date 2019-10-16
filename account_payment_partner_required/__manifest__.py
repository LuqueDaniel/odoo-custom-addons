# Copyright 2019 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Account Payment Partner Mandatory',
    'version': '11.0.1.0.0',
    'summary': """Makes the Partner Payment Mode and Partner Payment Terms
               fields mandatory.""",
    'author': 'Daniel Luque',
    'website': "https://github.com/LuqueDaniel/odoo-custom-addons",
    'license': 'AGPL-3',
    'category': 'Banking addons',
    'depends': ['account_payment_partner'],
    'data': [
        'views/res_partner_view.xml'
    ],
    'installable': True
}
