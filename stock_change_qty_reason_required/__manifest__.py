# Copyright 2021 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "Stock Change Quantity Reason Required",
    "author": "Daniel Luque",
    "license": "AGPL-3",
    "summary": "Makes the preset reason field required.",
    "website": "https://github.com/LuqueDaniel/odoo-custom-addons",
    "category": "Stock",
    "version": "12.0.1.0.1",
    "depends": ["stock_change_qty_reason"],
    "data": ["views/stock_inventory_view.xml", "views/stock_inventory_line_view.xml"],
    "installable": True,
}
