# -*- coding: utf-8 -*-

from openerp.tests import common


class TestContractCommon(common.TransactionCase):

    def setUp(self):
        super(TestContractCommon, self).setUp()
        
        self.ProductObj = self.env['product.product']
        self.PartnerObj = self.env['res.partner']
        self.ModelDataObj = self.env['ir.model.data']
        self.ContractObj = self.env['account.analytic.account']
        self.invoce_obj = self.env['account.invoice']
        # Model Data
        self.main_company = self.ModelDataObj.xmlid_to_res_id(
            'base.main_company'
            )
        self.main_partner = self.ModelDataObj.xmlid_to_res_id(
            'base.main_partner'
            )
        self.product_consultant = self.ModelDataObj.xmlid_to_res_id(
            'product.product_product_consultant'
            )
        self.uom_hour = self.ModelDataObj.xmlid_to_res_id(
            'product.product_uom_hour'
            )
        self.enero = self.ModelDataObj.xmlid_to_res_id(
            'contract_multiple_period.contract_month_1'
            )
        self.mayo = self.ModelDataObj.xmlid_to_res_id(
            'contract_multiple_period.contract_month_5'
            )
        self.junio = self.ModelDataObj.xmlid_to_res_id(
            'contract_multiple_period.contract_month_6'
            )
        self.julio = self.ModelDataObj.xmlid_to_res_id(
            'contract_multiple_period.contract_month_7'
            )
        self.months = [self.enero, self.junio, self.julio]

