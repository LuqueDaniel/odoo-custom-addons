# Copyright 2019 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class SaleOrder(models.Model):
    """Adds partner category_id field to sale order model."""
    _inherit = 'sale.order'

    partner_category_id = fields.Many2many(related='partner_id.category_id',
                                           string="Partner tags")
