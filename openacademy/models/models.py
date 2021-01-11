# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(string="Sessionin Title", required=True)
    start_date = fields.Date()
    duration = fields.Float(digit=(6, 2))
    seats = fields.Integer(string="Number Of Seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
