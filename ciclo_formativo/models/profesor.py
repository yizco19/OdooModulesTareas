# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'Profesor'

    name = fields.Char(string='Nombre', required=True)
    surname=fields.Char(string="Apellidos")
    dni=fields.Char(string="DNI")
    ciclo_ids = fields.Many2many('instituto.ciclo_formativo', string='Ciclos')
    modulo_ids = fields.One2many('instituto.modulo','profesor_id', string='Modulos')

