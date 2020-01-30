# Copyright 2019 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class AccountInvoice(models.Model):
    """Adds credit_policy field to Account Invoice model."""
    _inherit = 'account.invoice'

    credit_policy = fields.Char(related='partner_id.credit_policy')
