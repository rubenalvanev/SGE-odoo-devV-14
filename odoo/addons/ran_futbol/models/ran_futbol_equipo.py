from odoo import models, fields, api

class RanFutbolEquipo(models.Model):
    _name = 'ran_futbol.equipo'
    _description = 'Equipo'
    
    name = fields.Char('Nombre')
    dinero = fields.Float('Dinero')
    division = fields.Selection([
        ('0', 'Primera'),
        ('1', 'Segunda'),
        ('2', 'Tercera'),
        ('3', 'Cuarta')
    ], string='Division', default='1')
    fecha_ultimo_partido = fields.Date('Fecha del ultimo partido')

    jugador_ids = fields.One2many('ran_futbol.jugador', 'equipo_id', string='Jugadores')