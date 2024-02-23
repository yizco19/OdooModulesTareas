# -*- coding: utf-8 -*-
{
    'name': "Biblioteca ZY",  # Titulo del módulo
    'summary': "Gestionar comics :) (Version Ultimate)",  # Resumen de la funcionaliadad
    'description': """
Gestor de bibliotecas (Version Ultimate)
==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Zhi Yang",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        #Estos dos primeros ficheros:
        #1) El primero indica grupo de seguridad basado en rol
        #2) El segundo indica la politica de acceso del modelo
        #Mas información en https://www.odoo.com/documentation/14.0/es/developer/howtos/rdtraining/05_securityintro.html
        #Y en www.odoo.yenthevg.com/creating-security-groups-odoo/ 
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/biblioteca_comic.xml',
        'views/biblioteca_socio.xml',
        'views/biblioteca_ejemplar.xml',
        #Cargamos la vista de la biblioteca de comics
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
