from odoo import api, fields, models


class Paciente(models.Model):
    _name = "hospital.paciente"
    _description = "Modelo de paciente"
    _rec_name="nombre"
    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    sintoma = fields.Text(string="Sintoma")
    diagnostico = fields.Many2many('hospital.diagnostico', string='Diagnostico')

