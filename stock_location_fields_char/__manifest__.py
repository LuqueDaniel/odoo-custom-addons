# -*- coding: utf-8 -*-
# Copyright 2017-2018 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': "Stock Location Fields Char",
    'version': '0.1',
    'summary': """This addon replaces the `int` fields of the `stock.location` model with new ones of type `char`""",
    'description': """
    This addon replaces the `int` fields of the `stock.location` model with new ones of type `char
        Features:
            - Hides the fields `posx`,` posy` and `posz`. These fields     indicate the location in the locations (aisle, shelf, height).
            - Add the following fields: `x_posx`,` x_posy` and `x_posz`. These fields are alphanumeric, with a maximum size of 10 characters.
            - Modify the views to use the new fields instead of the ones by default.
    """,
    'author': "Daniel Luque",
    'website': "https://github.com/LuqueDaniel/odoo_custom_addons",
    'license': 'AGPL-3',
    'category': 'Warehouse Management',
    'depends': ['stock'],
    'data': [
        # Stock views
        'views/stock_location_views.xml',
    ],
    'installable': True
}
