from odoo import models, fields, api

class RanFutbolClasificacion(models.Model):
    _name = 'ran_futbol.clasificacion'
    _description = 'Clasificación de Equipos'

    competicion_id = fields.Many2one('ran_futbol.competicion', string='Competición')
    equipo_id = fields.Many2one('ran_futbol.equipo', string='Equipo')
    puntos = fields.Integer(string='Puntos', default=0)
    partidos_ganados = fields.Integer(string='Ganados', default=0)
    partidos_empatados = fields.Integer(string='Empatados', default=0)
    partidos_perdidos = fields.Integer(string='Perdidos', default=0)
    goles_favor = fields.Integer(string='Goles a favor', default=0)
    goles_contra = fields.Integer(string='Goles en contra', default=0)
    diferencia_goles = fields.Integer(string='Diferencia de goles', compute='_compute_diferencia')

    @api.depends('goles_favor', 'goles_contra')
    def _compute_diferencia(self):
        for record in self:
            record.diferencia_goles = record.goles_favor - record.goles_contra
