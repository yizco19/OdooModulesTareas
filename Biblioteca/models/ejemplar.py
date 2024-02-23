from odoo import models, fields

class Ejemplar(models.Model):
    _name = 'biblioteca.ejemplar'
    _description = 'Ejemplar de biblioteca'
    _order = 'fecha_alta desc, nombre'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True, index=True)
    fecha_alta = fields.Date('Fecha de alta')
    fecha_baja = fields.Date('Fecha de baja')
    comic_id = fields.Many2one('biblioteca.comic', string='Comic')
    socio_id = fields.Many2one('biblioteca.socio', string='Socio')
    