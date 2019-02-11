# -*- coding: utf-8 -*-
# Copyright 2017-2018 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Stock Location Fields Char',
    'version': '10.0.1.0.0',
    'summary': """This addon replaces the `int` fields of the
               `stock.location` model with new ones of type `char`""",
    'author': 'Daniel Luque',
    'website': "https://github.com/LuqueDaniel/odoo-custom-addons",
    'license': 'AGPL-3',
    'category': 'Warehouse Management',
    'depends': ['stock'],
    'data': [
        # Stock views
        'views/stock_location_views.xml',
    ],
    'installable': True
}
