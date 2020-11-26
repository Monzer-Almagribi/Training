# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': 'Hospital Management System',

    'description': """ A software to manage hospitl records   """,

    'author': "newbee",
    'category': 'Extra Tools',
    'version': '13.1.0.1',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': ['views/patient.xml',
     ],
}