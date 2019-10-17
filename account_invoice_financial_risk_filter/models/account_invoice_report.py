# Copyright 2019 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import fields, models


class AccountInvoiceReport(models.Model):
    """Adds credit_policy field to invoice report model."""
    _inherit = 'account.invoice.report'

    credit_policy = fields.Char(related='partner_id.credit_policy')
