# -*- coding: utf-8 -*- 
from odoo import api, fields, models 
from datetime import datetime
from odoo.exceptions import UserError, ValidationError

class validation_stock_picking(models.Model): 
    _inherit = "stock.picking" 
    _name ="button_granja"


    def enviar_granja(self):
    	raise ValidationError('SEGUIMOS TRABAJANDO')
 
