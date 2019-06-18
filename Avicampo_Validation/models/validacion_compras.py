# -*- coding: utf-8 -*- 
from odoo import api, fields, models 
from datetime import datetime 
from odoo.exceptions import UserError, ValidationError

class validation_purchase(models.Model): 
    _inherit = "purchase.order" 
    _name ="button_compra"
    

    def enviar_granja_compras(self):
    	raise ValidationError('SEGUIMOS TRABAJANDO')
 
