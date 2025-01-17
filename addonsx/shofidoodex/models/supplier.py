from odoo import models, fields, api

class DoodexSupplier (models.Model):
    _name = 'doodex.supplier'
    _description = 'doodex supplier'

    name = fields.Char(string='Nama Supplier')
    telp = fields.Char(string='No. Telp')
    cp = fields.Char(string='Contact Person')
    alamat = fields.Char(string='Alamat')
    

    barang_ids = fields.Many2many(comodel_name='barang.doodex', string='Supply Barang')
    