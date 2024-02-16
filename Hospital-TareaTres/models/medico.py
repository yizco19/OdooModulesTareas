# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Medico(models.Model):
    _name = "hospital.medico"
    _description = "Modelo de médico"
    _rec_name="nombre"

    nombre = fields.Char(string="Nombre")
    apellido = fields.Char(string="Apellido")
    colegiado = fields.Integer(string="Número de Colegiado")
    diagnostico = fields.Many2many('hospital.diagnostico', string='Diagnostico')
