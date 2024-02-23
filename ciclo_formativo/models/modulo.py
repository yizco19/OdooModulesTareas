# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Modulo(models.Model):
    _name = 'instituto.modulo'
    _description = 'Módulo'

    name = fields.Char(string='Modulo', required=True)
    ciclo_id = fields.Many2one('instituto.ciclo_formativo', string='Ciclo')
    alumno_ids = fields.Many2many('instituto.alumno', string='Alumnos')
    profesor_id = fields.Many2one('instituto.profesor', string='Profesores')






