from odoo import models, fields, api

class SgeLibreriaLibro(models.Model):
    _name = 'sge_libreria.libro'
    _description = 'Libro'

    name = fields.Char('Título')
    precio = fields.Float('Precio')
    ejemplares = fields.Integer('Ejemplares')
    fecha_compra = fields.Date('Fecha compra')
    segmano = fields.Boolean('Segunda mano')
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Malo')
    ], string='Estado', default='0')

    categoria_id = fields.Many2one('sge_libreria.categoria', string='Categoría')