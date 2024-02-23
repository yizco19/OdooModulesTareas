# -*- coding: utf-8 -*-

from odoo import models, fields, api
class CicloFormativo(models.Model):
    _name = 'instituto.ciclo_formativo'
    _description = 'Ciclo Formativo'

    name = fields.Char(string='Ciclo', required=True)
    # Otros campos del ciclo formativo
    modulo_ids = fields.One2many('instituto.modulo', 'ciclo_id', string='Modulos')
    alumno_ids = fields.One2many('instituto.alumno', 'ciclo_id', string='Alumnos')
    profesor_ids = fields.Many2many('instituto.profesor', string='Profesores') 