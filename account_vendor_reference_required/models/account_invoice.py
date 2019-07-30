# -*- coding: utf-8 -*-
# Copyright 2019 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo import fields, models


class AccountInvoice(models.Model):
    """Makes the Vendor Reference field mandatory."""
    _inherit = 'account.invoice'

    # Overrides base field
    reference = fields.Char(string='Vendor Reference', copy=False,
                            help="The partner reference of this invoice.",
                            readonly=True, required=True,
                            states={'draft': [('readonly', False)]})
