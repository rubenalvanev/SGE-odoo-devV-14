from odoo import models, fields, api

class RanFutbolEstadisticas(models.Model):
    _name = 'ran_futbol.estadisticas'
    _description = 'Estadisticas'
    
    name = fields.Char('Estadisticas')
    jugador_id = fields.Many2one('ran_futbol.jugador', string='Jugador')
    goles = fields.Integer('Goles')
    imagen = fields.Image('Imagen', max_width='10', max_height='10')
    partidos = fields.Integer('Partidos')
    mins_jugados = fields.Integer('Minutos jugados')
    tarjetas = fields.Integer('Tarjetas')
    rendimiento = fields.Selection([
        ('0', '⭐'),
        ('1', '⭐⭐'),
        ('2', '⭐⭐⭐'),
        ('3', '⭐⭐⭐⭐'),
        ('4', '⭐⭐⭐⭐⭐')
    ], string='Rendimiento', default='0')