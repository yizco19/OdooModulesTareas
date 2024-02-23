from odoo import models, fields

class Socio(models.Model):
    _name = 'biblioteca.socio'
    _description = 'Información de Socios'
    _rec_name = 'nombre'
    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    identificador = fields.Char(string='Identificador', required=True)
    ejemplar_ids = fields.One2many('biblioteca.ejemplar', 'socio_id', string='Ejemplares')
