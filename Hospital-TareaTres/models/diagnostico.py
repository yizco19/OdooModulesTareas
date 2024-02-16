from odoo import api, fields, models


class Diagnostico(models.Model):
    _name = "hospital.diagnostico"
    _description = "Modelo de diagnóstico"

    paciente_ids = fields.Many2many('hospital.paciente', string='Pacientes')
    medico_ids = fields.Many2many('hospital.medico', string='Medicos')
