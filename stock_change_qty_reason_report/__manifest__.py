# Copyright 2021 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "Stock Change Quantity Reason Report",
    "author": "Daniel Luque",
    "license": "AGPL-3",
    "summary": "Adds stock change reason report.",
    "website": "https://github.com/LuqueDaniel/odoo-custom-addons",
    "category": "Stock / Report",
    "version": "12.0.1.0.3",
    "depends": ["stock_change_qty_reason"],
    "data": ["report/stock_reason_report_view.xml", "security/ir.model.access.csv"],
    "installable": True,
}
