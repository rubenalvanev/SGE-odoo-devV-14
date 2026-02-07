from odoo import models, fields, api

class RanFutbolCompeticion(models.Model):
    _name = 'ran_futbol.competicion'
    _description = 'Competición'
    
    name = fields.Char('Nombre')
    tipo = fields.Selection([
        ('0', 'Liga'),
        ('1', 'Copa'),
        ('2', 'Torneo'),
    ], string='Tipo', default='0')
    clasificacion_ids = fields.One2many('ran_futbol.clasificacion', 'competicion_id', string='Clasificación')
    equipo_ids = fields.Many2many('ran_futbol.equipo', string='Equipos de la competicion')