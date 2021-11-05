# -*- coding: utf-8 -*-

from odoo import models, fields, api


class import_product(models.Model):
    _inherit = 'product.template'
    _description = 'Campos de Importacion comercial'

    tariff_percentage = fields.Float(string='Porcentaje de arancel',
                                          help="Porcentaje Impuesto del Arancel")
    official_mexican_standards = fields.Many2one('l10n_mx_edi_noms',string='NOMS', help="Normas Oficiales Mexicanas")

class import_product_purchase(models.Model):
    _inherit = 'purchase.order'
    _description = 'Campos necesarios para el manejo de Importaciones WB'

    freigth = fields.Monetary(string='Flete (USD)', help='Costo de flete')
    sea_freight = fields.Monetary(string='Flete Maritimo (USD)')
    land_freight = fields.Monetary(string='Flete terrestre')
    general_import_tax = fields.Monetary(string='IGI', help='Normativa al Comercio Exterior')
    value_added_tax = fields.Monetary(string='IVA')
    customs_processing_right = fields.Monetary(string='DTA')
    prevalidation = fields.Monetary(string='PRV')
    vat_prevalidation = fields.Monetary(string='IVA / PRV')
    customs_charges = fields.Monetary(string='Gastos en aduana')
    storages = fields.Monetary(string='Almacenajes')
    delays = fields.Monetary(string='Demoras')
    salary_customs_agents = fields.Monetary(string='Honorarios Agente Aduanal')

class l10nmxnoms(models.Model):
    _name = 'l10n_mx_edi_noms'
    _description = 'Catalogo de Normas Mexicanas para importacion'

    code = fields.Char(string='Codigo')
    name = fields.Char(string='Nombre')