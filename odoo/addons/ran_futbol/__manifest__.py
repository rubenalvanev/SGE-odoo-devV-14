# -*- coding: utf-8 -*-
{
    'name': "ran_futbol",

    'summary': "Gestión de equipos de futbol",

    'description': """
Con esta aplicación podras gestionar varios equipos y jugadores ligados a estos
    """,

    'author': "Rubén Álvarez",
    'website': "https://github.com/rubenalvanev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ran_futbol_jugador.xml',
        'views/ran_futbol_equipo.xml',
        'views/ran_futbol_estadisticas.xml',
        'views/ran_futbol_clasificacion.xml',
        'views/ran_futbol_competicion.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

