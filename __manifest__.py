# -*- coding: utf-8 -*-
{
    'name': "Web Sale Ext",

    'summary': """
        Demostración modulo compatible para Odoo15
        Sales, Website
        """,

    'description': """
        Demostración modulo compatible para Odoo15
        Sales, Website
    """,

    'author': "Open Codev SAC",
    'website': "http://www.opencodev.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','website_sale','contacts'],

    # always loaded
    'data': [
        'views/sale_order_view.xml',
        'views/website_sale.xml',
        'views/res_partner.xml',
    ],
}
