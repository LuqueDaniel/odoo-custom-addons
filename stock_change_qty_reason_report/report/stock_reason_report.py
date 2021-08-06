# Copyright 2021 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo import api, fields, models, tools

from odoo.addons import decimal_precision as dp


class StockReasonReport(models.Model):
    _name = "stock.reason.report"
    _description = "Stock reason report"
    _rec_name = "product_id"
    _auto = False

    product_id = fields.Many2one("product.product", string="Product", readonly=True)
    inventory_line_id = fields.Many2one(
        "stock.inventory.line", string="Inventory line", readonly=True
    )
    location_id = fields.Many2one("stock.location", string="Location", readonly=True)
    company_id = fields.Many2one("res.company", string="Company", readonly=True)
    category_id = fields.Many2one("product.category", string="Category", readonly=True)
    preset_reason_id = fields.Many2one(
        "stock.inventory.line.reason", string="Stock change reason", readonly=True
    )
    in_date = fields.Datetime("Date of change", readonly=True)
    difference_qty = fields.Float(
        string="Quantity difference",
        readonly=True,
        digits=dp.get_precision("Product Unit of Measure"),
    )
    unit_value = fields.Float(
        "Unit value", digits=dp.get_precision("Product Price"), readonly=True
    )
    total_value = fields.Float(
        "Total value", digits=dp.get_precision("Product Price"), readonly=True
    )

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(
            f"""CREATE or REPLACE VIEW {self._table} as (
                {self._select()}
                {self._from()}
            )"""
        )

    def _select(self):
        return """
            SELECT
                il.id as id,
                il.id as inventory_line_id,
                il.product_id AS product_id,
                il.location_id AS location_id,
                il.company_id AS company_id,
                il.preset_reason_id AS preset_reason_id,
                il.create_date AS in_date,
                il.product_qty - il.theoretical_qty AS difference_qty,
                pt.categ_id AS category_id,
                pr.value_float AS unit_value,
                pr.value_float * (il.product_qty - il.theoretical_qty) AS total_value
        """

    def _from(self):
        return """
            FROM stock_inventory_line il
            JOIN product_product pp ON pp.id = il.product_id
            JOIN product_template pt ON pt.id = pp.product_tmpl_id
            JOIN ir_property pr ON (pr.res_id = 'product.product,' || pp.id)
        """

    @api.model
    def read_group(
        self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True
    ):
        groups = {
            "location_id",
            "company_id",
            "preset_reason_id",
            "category_id",
            "in_date",
        }
        if (groups & set(groupby)) or len(groupby) == 0:
            if "unit_value" in fields:
                fields.remove("unit_value")
            if "difference_qty" in fields:
                fields.remove("difference_qty")
        return super().read_group(
            domain, fields, groupby, offset, limit=limit, orderby=orderby, lazy=lazy
        )
