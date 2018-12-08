# Copyright 2017-2018 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import UserError


NO_VAT_MSG = _("The VAT for this customer is not defined. The customer should have a VAT.")


class CustomSaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def _prepare_invoice(self):
        "Adds Vat check before create an invoice."
        res = super(CustomSaleOrder, self)._prepare_invoice()
        # Prevents invoicing if the customer has not assigned VAT
        if not self.partner_id.vat:
            raise UserError(NO_VAT_MSG)
        return res
