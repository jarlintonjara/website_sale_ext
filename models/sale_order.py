# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"
    to_check = fields.Boolean(string="To check", help="Check", copy=False)