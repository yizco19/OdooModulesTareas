# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas Uno",

    'summary': """
    Una sencilla lista de tareas""",
    
    'description': """
    Este módulo crea una sencilla lista de tareas para gestionar tareas pendientes.
    """,

    'author': "Zhi Yang",
    'website': "https://www.youtube.com/watch?v=IeJFxmCG2Qs",
    
    # Indicamos que es una aplicación
    'application': True,
    'category': 'Project',
    # En la siguiente URL se indica qué categorías pueden usarse:
    # https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # Vamos a utilizar la categoría Productivity
    'category': 'Productivity',
    
    'version': '0.1',

    # Indicamos la lista de módulos necesarios para que este funcione correctamente.
    # En este ejemplo, solo depende del módulo "base".
    'depends': ['base'],

    # Esto siempre se carga
    'data': [
        # El primer archivo indica la política de acceso del modelo.
        # Más información en https://www.odoo.com/documentation/14.0/es/developer/howtos/rdtraining/05_securityintro.html
        'security/ir.model.access.csv',
        
        # Cargamos las vistas y las plantillas.
        'views/views.xml',
    ]
}
