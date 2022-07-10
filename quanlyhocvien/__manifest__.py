# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'School Module',
    'version' : '1.1',
    'summary': 'School',
    'sequence': 15,
    'description': """
    school
    """,
    'category': '',
    'website': '',
    'images' : [],
    'depends' : [],
    'data': [
        "security/ir.model.access.csv",
        "views/student_views.xml",
    ],
    'demo': [],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '',
}