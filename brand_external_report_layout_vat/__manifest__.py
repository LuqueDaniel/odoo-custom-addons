# Copyright 2020 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "Brand External Report Layout Vat",
    "summary": """Display company vat in brand external layout.""",
    "description": """Extends `web.external_layout_ *` views to display
    company VAT in brand's external layouts.
    """,
    "author": "Daniel Luque",
    "license": "AGPL-3",
    "website": "https://github.com/LuqueDaniel/odoo-custom-addons",
    "version": "12.0.1.0.0",
    "depends": ["brand_external_report_layout"],
    "data": ["views/external_layouts.xml"],
}
