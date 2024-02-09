# models/doctor.py
from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Information'

    name = fields.Char(string='Name', required=True)
    registration_number = fields.Char(string='Registration Number', required=True)
    diagnosis_ids = fields.Many2many('hospital.diagnosis', string='Diagnoses')
