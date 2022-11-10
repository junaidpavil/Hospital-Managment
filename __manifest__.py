# -*- coding: utf-8 -*-


{
    'name': 'Hospital Managment',
    'version': '1.0.0',
    'category': 'Hospital',
    'author':'odox',
    'summary': 'Hospital Management System',
    'description': """Hospital Management System""",
    'sequence':-100,
    'depends': ['mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/cancel_appointment_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
         'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/today_view.xml',
        'views/patient_tag_view.xml',
        'reports/report.xml',
        'reports/patient_card.xml',

    ],
    'demo': [],
    'application':True,
    'auto_install': False,
    'assets': {},
}
