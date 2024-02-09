# models/diagnosis.py
from odoo import models, fields

class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis Information'

    name = fields.Char(string='Diagnosis Name', required=True)
    description = fields.Text(string='Description')
    patient_ids = fields.Many2many('hospital.patient', string='Patients')
    doctor_ids = fields.Many2many('hospital.doctor', string='Doctors')
