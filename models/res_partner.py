# -*- coding: utf-8 -*-

from odoo import models, fields

class Partner(models.Model):
    _inherit = "res.partner"
    passport = fields.Char(string="Passport", help="Passport", copy=False)