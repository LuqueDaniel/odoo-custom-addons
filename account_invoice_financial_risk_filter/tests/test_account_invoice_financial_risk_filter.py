# Copyright 2019 Daniel Luque
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo.tests import common


@common.at_install(False)
@common.post_install(True)
class TestAccountInvoiceFinancialRiskFilter(common.TransactionCase):
    def test_account_invoice(self):
        if "credit_policy" not in self.env["account.invoice"]._fields:
            raise Exception("`credit_policy` does not exist")

    def test_account_invoice_report(self):
        if "credit_policy" not in self.env["account.invoice.report"]._fields:
            raise Exception("`credit_policy` does not exist")
