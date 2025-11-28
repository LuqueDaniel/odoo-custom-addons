# Copyright 2020 ACT Bricolaje y Decoración
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import fields, models


class ResBrand(models.Model):
    _inherit = "res.brand"

    vat = fields.Char(related="company_id.vat", store=True)
