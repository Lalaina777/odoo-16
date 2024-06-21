# -*- coding: utf-8 -*-
from odoo import api, fields, models



# This is a class that defines the model for hospital patients
class HospitalPatient(models.Model):
    # This sets the name of the model to "hospital.patient"
    _name = "hospital.patient"
    # This sets the description of the model to "Patient Records"
    _description = "Patient Records"
    
    # This defines a required character field for the patient's name
    name = fields.Char(string='Name', required=True)
    
    # This defines an integer field for the patient's age
    age = fields.Integer(string='Age')
    
    # This defines a boolean field to indicate if the patient is a child or not, with a default value of False
    is_child = fields.Boolean(string="Is Child?", default=False)
    
    # This defines a text field for any notes about the patient
    notes = fields.Text(string="Notes")
    
    # This defines a selection field for the patient's gender, with options for 'male', 'female', and 'other'
    # The field is required and has a default value of 'male'
    _description = "Patient Records"
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    is_child = fields.Boolean(string="Is Child?", default=False)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", required=True, default='male')
    