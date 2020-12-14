# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class HospitaPatient(models.Model):
	_name = 'hospital.patient'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = 'Patient Record'
	_rec_name = 'patient_name'

	patient_name = fields.Char(string='Name', required=True)
	patient_age = fields.Integer(string='Age')
	notes = fields.Text(string='Note')
	Image = fields.Binary(string='Image')
	name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
