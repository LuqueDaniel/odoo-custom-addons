# Copyright 2020 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class AccountMove(models.Model):
    """Make `brand_id` editable on account moves (invoices)."""

    _inherit = "account.move"

    brand_id = fields.Many2one(
        states={
            "posted": [("readonly", False)],
            # Cancelled moves
            "cancel": [("readonly", False)],
        }
    )
