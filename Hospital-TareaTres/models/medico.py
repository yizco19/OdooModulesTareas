# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Medico(models.Model):
    _name = "hospital.medico"
    _description = "Modelo de médico"

    nombre = fields.Char(string="Nombre")
    apellido = fields.Char(string="Apellido")
    colegiado = fields.Integer(string="Número de Colegiado")