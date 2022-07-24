from odoo import fields, models, api


gender_list = [
    ('unknown','Unknown'),
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
]

class Students(models.Model):
    _name = "school.students"
    
    name = fields.Char("Student Name")
    student_code = fields.Char("Students Code")
    date_of_birth = fields.Date("Date Of Birth")
    native_country = fields.Many2one("res.country.state", "Native Country", domain="[('country_id','=',241)]")
    identity_card = fields.Integer("Identity Card")
    gender = fields.Selection(gender_list,"Gender")
    phone = fields.Char("Phone")
    class_id = fields.Many2one("school.classes", "Class")

