# -*- coding: utf-8 -*-
# Copyright 2019 Daniel Luque (https://github.com/LuqueDaniel)
# Based on the module pos_margin (v11.0) by Sylvain LE GAL
#  (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models, tools


class PosOrderReport(models.Model):
    _inherit = 'report.pos.order'

    margin_total = fields.Float(string='Margin Total')
    margin_rate = fields.Float(string='Margin Rate', group_operator='avg')

    def _select(self):
        return """
            SELECT
                MIN(l.id) AS id,
                COUNT(*) AS nbr_lines,
                s.date_order AS date,
                SUM(l.qty) AS product_qty,
                SUM(l.qty * l.price_unit) AS price_sub_total,
                SUM((l.qty * l.price_unit) * (100 - l.discount) / 100)
                AS price_total,
                SUM((l.qty * l.price_unit) * (l.discount / 100))
                AS total_discount,
                (SUM(l.qty*l.price_unit)/SUM(l.qty * u.factor))::decimal
                AS average_price,
                SUM(cast(to_char(date_trunc('day',s.date_order) -
                date_trunc('day',s.create_date),'DD') AS INT))
                AS delay_validation,
                s.id as order_id,
                s.partner_id AS partner_id,
                s.state AS state,
                s.user_id AS user_id,
                s.location_id AS location_id,
                s.company_id AS company_id,
                s.sale_journal AS journal_id,
                l.product_id AS product_id,
                pt.categ_id AS product_categ_id,
                p.product_tmpl_id,
                ps.config_id,
                pt.pos_categ_id,
                pc.stock_location_id,
                s.pricelist_id,
                s.session_id,
                s.invoice_id IS NOT NULL AS invoiced,
                SUM(l.margin) as margin_total,
                (SUM(l.margin / nullif(l.qty,0)) * 100 /
                SUM(nullif(l.purchase_price,0)))::decimal as margin_rate
        """

    def _from(self):
        return """
            FROM pos_order_line AS l
                LEFT JOIN pos_order s ON (s.id=l.order_id)
                LEFT JOIN product_product p ON (l.product_id=p.id)
                LEFT JOIN product_template pt ON (p.product_tmpl_id=pt.id)
                LEFT JOIN product_uom u ON (u.id=pt.uom_id)
                LEFT JOIN pos_session ps ON (s.session_id=ps.id)
                LEFT JOIN pos_config pc ON (ps.config_id=pc.id)
        """

    def _group_by(self):
        return """
            GROUP BY
                s.id, s.date_order, s.partner_id,s.state, pt.categ_id,
                s.user_id, s.location_id, s.company_id, s.sale_journal,
                s.pricelist_id, s.invoice_id, s.create_date, s.session_id,
                l.product_id,
                pt.categ_id, pt.pos_categ_id,
                p.product_tmpl_id,
                ps.config_id,
                pc.stock_location_id
        """

    def _having(self):
        return """
            HAVING
                SUM(l.qty * u.factor) != 0
        """

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
        CREATE OR REPLACE VIEW %s AS (
            %s
            %s
            %s
            %s
        )
        """ % (self._table, self._select(), self._from(), self._group_by(),
               self._having())
        )
