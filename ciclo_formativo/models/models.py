# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CicloFormativo(models.Model):
    _name = 'instituto.ciclo_formativo'
    _description = 'Ciclo Formativo'

    name = fields.Char(string='Ciclo', required=True)
    # Otros campos del ciclo formativo
    modulo_ids = fields.One2many('instituto.modulo', 'ciclo_id', string='Modulos')


class Modulo(models.Model):
    _name = 'instituto.modulo'
    _description = 'Módulo'

    name = fields.Char(string='Modulo', required=True)
    ciclo_id = fields.Many2one('instituto.ciclo_formativo', string='Ciclo')
    alumno_ids = fields.Many2many('instituto.alumno', string='Alumnos')
    profesor_id = fields.Many2one('instituto.profesor', string='Profesores')


class Alumno(models.Model):
    _name = 'instituto.alumno'
    _description = 'Alumno'

    name = fields.Char(string='Nombre', required=True)
    surname=fields.Char(string="Apellidos")
    dni=fields.Char(string="DNI")
    modulo_ids = fields.Many2many('instituto.modulo', string='Modulos')


class Profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'Profesor'

    name = fields.Char(string='Nombre', required=True)
    surname=fields.Char(string="Apellidos")
    dni=fields.Char(string="DNI")
    modulo_ids = fields.One2many('instituto.modulo','profesor_id', string='Modulos')
