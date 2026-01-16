from odoo import models, fields, api

class SgeLibreriaCategoria(models.Model):
    _name = 'sge_libreria.categoria'
    _description = 'Categoria'
    
    name = fields.Char('Título')
    description = fields.Char('Descripcion')

    libro_ids = fields.One2many('sge_libreria.libro', 'categoria_id', string='Libros')