# Copyright 2019 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class AccountMoveInherit(models.Model):
    """Adds credit_policy field to Account Move (invoices)."""

    _inherit = "account.move"

    credit_policy = fields.Char(related="partner_id.credit_policy")
