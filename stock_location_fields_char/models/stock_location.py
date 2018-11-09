# -*- coding: utf-8 -*-
# Copyright 2017-2018 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import models, fields


class CustomStockLocation(models.Model):
    """This class inherits and modifies the stock.location model."""
    _inherit = 'stock.location'

    # New fields
    x_posx = fields.Char('Corridor (X)', size=10,
                         help="Optional localization details, for information \
                         purpose only")
    x_posy = fields.Char('Shelves (Y)', size=10,
                         help="Optional localization details, for information \
                         purpose only")
    x_posz = fields.Char('Height (Z)', size=10,
                         help="Optional localization details, for information \
                         purpose only")
