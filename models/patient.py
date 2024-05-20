# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Records"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    is_child = fields.boolean(string="Is Child ?")
    notes = fields.Text(string="Notes")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    