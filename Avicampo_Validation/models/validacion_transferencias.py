# -*- coding: utf-8 -*- 
from odoo import api, fields, models 
from datetime import datetime
from odoo.exceptions import UserError, ValidationError


class granjasencargado(models.Model):
	_inherit = "stock.warehouse"	
	_name = "granja.encargado"

	granja = fields.Many2one('stock.warehouse', string="Granja")
	granja_abr = fields.Char(required=True, string = "Abreviatura")
	encargado = fields.Many2many('res.users', string="Encargado")

	@api.one
	@api.depends('granja'):
	def _compute_granja_abr(self):
		self.granja_abr = self.stock.warehouse.code



class validation_stock_picking(models.Model): 
    _inherit = "stock.picking"


    aprobado_url = fields.Char()
    rechazado_url = fields.Char()


    def enviar_granja(self):
    	raise ValidationError('SEGUIMOS TRABAJANDO')


 
