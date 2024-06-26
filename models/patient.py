# -*- coding: utf-8 -*-
from odoo import api, fields, models


# This is a class that defines the model for hospital patients
class HospitalPatient(models.Model):
    # This sets the name of the model to "hospital.patient" 1239
    _name = "hospital.patient"
    _inherit = 'mail.thread'
    _description = "Patient Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string="Is Child?", default=False, tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", tracking=True)

    @api.onchange('age')
    def onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False
        