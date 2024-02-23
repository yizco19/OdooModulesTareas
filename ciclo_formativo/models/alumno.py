# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Alumno(models.Model):
    _name = 'instituto.alumno'
    _description = 'Alumno'

    name = fields.Char(string='Nombre', required=True)
    surname=fields.Char(string="Apellidos")
    dni=fields.Char(string="DNI")
    modulo_ids = fields.Many2many('instituto.modulo', string='Modulos')
    ciclo_id = fields.Many2one('instituto.ciclo_formativo', string='Ciclo')

    primerProfesor = fields.Many2one('instituto.profesor',
                                     related='modulo_ids.profesor_id',
                                     string='Primer Profesor',readonly=True)
    
    
    lista_modulos = fields.One2many('instituto.modulo',
                                     related='primerProfesor.modulo_ids',
                                  string='Lista de Modulos',
                                    readonly=True)
    lista_profesores= fields.Many2many('instituto.profesor', 
                                      related='ciclo_id.profesor_ids',
                                      string='Lista de Profesores',
                                      readonly=True)
    
