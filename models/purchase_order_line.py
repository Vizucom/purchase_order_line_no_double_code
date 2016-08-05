# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class PurchaseOrderLine(osv.Model):

    _inherit = 'purchase.order.line'

    def onchange_product_id(self, cr, uid, ids, pricelist_id, product_id, qty, uom_id,
            partner_id, date_order=False, fiscal_position_id=False, date_planned=False,
            name=False, price_unit=False, context=None):
        ''' After the onchange has constructed the contents for the name field,
        check if the code put to the brackets is the same as the product's internal reference
        (i.e. not the supplier code). If so, remove it from the name field '''
        res = super(PurchaseOrderLine, self).onchange_product_id(cr, uid, ids, pricelist_id, product_id, qty, uom_id,
                partner_id, date_order, fiscal_position_id, date_planned,
                name, price_unit, context)

        given_name = res['value'].get('name', False)

        if product_id and given_name and all(b in given_name for b in ['[', ']']):
            product = self.pool.get('product.product').browse(cr, uid, product_id, context)

            # Extract the code that Odoo has put between brackets
            given_code = given_name.split('[', 1)[-1].split(']', 1)[0]

            # Compare the codes -- if identical to the internal reference, remove it from the name field
            if given_code == product.default_code:
                res['value']['name'] = given_name.split('] ',1)[1]

        return res
