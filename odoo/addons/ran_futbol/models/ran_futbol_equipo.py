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
    goles = fields.Integer(string="Goles del equipo", compute="_goles_totales", store=True)
    competicion_ids = fields.Many2many('ran_futbol.competicion',relation='ran_futbol_rel_equipo_competicion', string='Competiciones de los equipos')
    fecha_ultimo_partido = fields.Date('Fecha del ultimo partido')
    imagen = fields.Image('Imagen', max_width=100, max_height=100)

    jugador_ids = fields.One2many('ran_futbol.jugador', 'equipo_id', string='Jugadores')

    _sql_constraints = [
        ('equipo_nombre_unico',
         'unique(name)',
         'Ya existe un equipo con este nombre.')
    ]

    @api.depends('jugador_ids.estadisticas_ids.goles')
    def _goles_totales(self):
        for equipo in self:
            total = 0
            for jugador in equipo.jugador_ids:
                total += sum(jugador.estadisticas_ids.mapped('goles'))
            equipo.goles = total