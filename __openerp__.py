# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2016- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Avoid double internal reference for PO lines',
    'category': 'Purchase',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['purchase'],
    'description': """
Avoid double internal reference for PO lines
============================================
 * By default Odoo adds the product's code to the description field on PO lines
 * This is useful mainly when the line's product has a different supplier code. If it doesn't, both Product and Description fields contain the code, which can be unwanted when creating prints.
 * This module checks the suggested Description field contents - an internal reference gets removed from it, but asupplier code remains as normal.
""",
    'data': []
}
