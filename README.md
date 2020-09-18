![Odoo Logo](/setup/odoo_logo.png)
# Odoo Custom Addons

[![Build Status](https://travis-ci.com/LuqueDaniel/odoo-custom-addons.svg?branch=12.0)](https://travis-ci.com/LuqueDaniel/odoo-custom-addons)

This repository contains addons that extend / modify parts of
**[Odoo](https://www.odoo.com/)** ERP.

## Addons list

* [account_cancel_permission](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/account_cancel_permission)
  * Only shows the button to cancel invoices, payments and bank statements to
      users with **Cancel Journal Entries** permission.
* [account_invoice_financial_risk_filter](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/account_invoice_financial_risk_filter)
  * Adds the ability to filter invoices through the customer's policy field.
* [account_invoice_payment_partner_required](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/account_invoice_payment_partner_required)
  * Makes the Payment Mode and Payment Terms fields of the invoice mandatory.
* [account_payment_partner_required](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/account_payment_partner_required)
  * Makes the Partner Payment Mode and Partner Payment Terms fields mandatory.
* [account_vendor_reference_required](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/account_vendor_reference_required)
  * Makes the Vendor Reference field mandatory.
* [brand_external_report_layout_vat](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/brand_external_report_layout_vat)
  * Display company vat in brand external layout.
* [hide_cost_margin](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/hide_cost_margin)
  * Hides the cost and margin prices for all users who don't have the
      `Show costs and margins` permission.
* [l10n_es_gdpr_notification](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/l10n_es_gdpr_notification)
  * summary": """Adds GDPR notification to documents
* [partner_tag_append_model](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/partner_tag_append_model)
  * Adds partner tag field to invoices and sale orders.
* [stock_analysis_valuation](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/stock_analysis_valuation)
  * Adds current unit cost and inventory value to Stock Analysis report
* [vat_checker](https://github.com/LuqueDaniel/odoo-custom-addons/tree/12.0/vat_checker)
  * Check if the customer has a VAT before creating an invoice from a sale
    order.

## License

[**AGPL-3.0**](http://www.gnu.org/licenses/agpl)

## Thanks to

* [**OCA** Odoo Community Association](https://github.com/OCA)
