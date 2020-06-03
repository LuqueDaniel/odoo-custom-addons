# Copyright 2020 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    brand_id = fields.Many2one(
        states={
            "open": [("readonly", False)],
            "in_payment": [("readonly", False)],
            "paid": [("readonly", False)],
            "cancel": [("readonly", False)],
        }
    )
