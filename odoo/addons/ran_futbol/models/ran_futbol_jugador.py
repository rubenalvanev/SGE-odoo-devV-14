from odoo import models, fields, api

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