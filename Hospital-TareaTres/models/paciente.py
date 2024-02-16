from odoo import api, fields, models


class Paciente(models.Model):
    _name = "hospital.paciente"
    _description = "Modelo de paciente"
    
    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    sintoma = fields.Text(string="Sintoma")

