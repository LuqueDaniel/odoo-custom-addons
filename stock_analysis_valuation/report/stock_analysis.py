# Copyright 2020 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, fields, models


class StockAnalysis(models.Model):
    _inherit = "stock.analysis"
    _auto = False

    cost = fields.Float(string="Unit Cost", readonly=True)
    stock_value = fields.Float(string="Stock Value", readonly=True)

    @api.model_cr
    def init(self):
        super().init()
        # Get creation query of the view
        self.env.cr.execute(f"SELECT pg_get_viewdef('{self._table}'::regclass::oid)")
        original_query = self.env.cr.fetchall()[0][0].replace(";", "")

        self._cr.execute(
            f"""CREATE OR REPLACE VIEW {self._table} as (
            SELECT
                origin.*,
                pr.value_float AS cost,
                pr.value_float * origin.quantity AS stock_value
            FROM (
                {original_query}
            ) AS origin
            JOIN ir_property pr
                ON pr.res_id = CONCAT(
                    'product.product,', CAST(origin.product_id AS text)
                )
            )"""
        )

    @api.model
    def read_group(
        self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True
    ):
        if ("categ_id" in groupby or "location_id" not in groupby) and "cost" in fields:
            fields.remove("cost")
        return super().read_group(
            domain, fields, groupby, offset, limit=limit, orderby=orderby, lazy=lazy
        )
