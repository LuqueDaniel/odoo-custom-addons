# Copyright 2020 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    brand_id = fields.Many2one(
        states={
            "sent": [("readonly", False)],
            "sale": [("readonly", False)],
            "done": [("readonly", False)],
            "cancel": [("readonly", False)],
        }
    )
