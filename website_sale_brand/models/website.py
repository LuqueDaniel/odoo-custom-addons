# Copyright 2020 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, models


class ModuleName(models.Model):
    _inherit = "website"

    @api.multi
    def _prepare_sale_order_values(self, partner, pricelist):
        """Extends website sale order to adds brand."""
        res = super()._prepare_sale_order_values(partner, pricelist)
        brand = (
            self.salesteam_id.brand_id
            or partner.parent_id.team_id.brand_id
            or partner.team_id.brand_id
        )
        if brand:
            res["brand_id"] = brand.id
        return res
