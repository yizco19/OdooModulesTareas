# __manifest__.py
{
    'name': "Hospital-TareaTres",
    'summary': "Tarea 3-Módulo de gestión de pacientes, médicos y diagnósticos en un hospital",
    'description': """
Este módulo permite gestionar pacientes, médicos y diagnósticos en un hospital..
    """,
    'author': "Zhi Yang",
    'website': "https://www.yourcompany.com",
    'category': 'Healthcare',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/diagnosis_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
