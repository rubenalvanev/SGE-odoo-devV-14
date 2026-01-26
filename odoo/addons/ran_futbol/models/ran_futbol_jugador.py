from odoo import models, fields, api
from odoo.exceptions import ValidationError

class RanFutbolJugador(models.Model):
    _name = 'ran_futbol.jugador'
    _description = 'Jugadores'
    
    name = fields.Char('Nombre')
    numero_camiseta = fields.Integer('Numero')
    anio = fields.Integer('Año de nacimiento')
    fecha_llegada = fields.Date('Fecha del ultimo partido')
    posicion = fields.Selection([
        ('0', 'Portero'),
        ('1', 'Defensa'),
        ('2', 'Medio'),
        ('3', 'Delantero')
    ], string='Posicion', default='2')

    equipo_id = fields.Many2one('ran_futbol.equipo', string='Equipo')
    estadisticas_ids = fields.One2many('ran_futbol.estadisticas', 'jugador_id', string='Estadisticas')

    @api.constrains('equipo_id')
    def _check_jugador_unico_equipo(jug):
        for jugador in jug:
            if jugador.equipo_id:
                jugadores = jug.search([
                    ('id', '!=', jugador.id),
                    ('equipo_id', '=', jugador.equipo_id.id),
                    ('name', '=', jugador.name)
                ])
                if jugadores:
                    raise ValidationError(
                        'Un jugador no puede estar en dos equipos distintos.'
                    )