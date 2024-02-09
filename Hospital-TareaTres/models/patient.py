# models/patient.py
from odoo import models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Information'

    name = fields.Char(string='Name', required=True)
    symptoms = fields.Text(string='Symptoms')
    diagnosis_ids = fields.Many2many('hospital.diagnosis', string='Diagnoses')
