# __manifest__.py
{
    'name': "Hospital-ZY",
    'summary': "Tarea 3 - Módulo de gestión de pacientes, médicos y diagnósticos en un hospital",
    'description': """
Este módulo permite gestionar pacientes, médicos y diagnósticos en un hospital.
    """,
    'author': "Zhi Yang",
    'website': "https://www.yourcompany.com",
    'category': 'Health',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        
        'security/ir.model.access.csv',
        'views/paciente_views.xml',
        'views/medico_views.xml',
        'views/diagnostico_views.xml'
    ],
    'application': True,
}
