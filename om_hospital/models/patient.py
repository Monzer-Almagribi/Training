# -*- coding: utf-8 -*-

from odoo import models, fields

class HospitaPatient(models.Model):
	_name = 'hospita.patient'
	_description = 'Patient Record'

	patient_name = fields.Char(string='Name', required=True)
	patient_age = fields.Integer(string='Age')
	notes = fields.Text(string='Note')
	Image = fields.Binary(string='Image')
