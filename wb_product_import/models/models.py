# -*- coding: utf-8 -*-

from odoo import models, fields, api


class import_product(models.Model):
    _inherit = 'product.template'
    _description = "Campos de Importacion comercial"

    tariff_fraction = fields.Char("Fracción Arancelaria")
    tariff_percentage = fields.Float(string='Porcentaje de arancel',
                                          help="Porcentaje Impuesto del Arancel")
    official_mexican_standards = fields.Char(string='NOMS', help="Normas Oficiales Mexicanas")
    freigth = fields.Monetary(string='Flete (USD)')
    general_import_tax = fields.Monetary(string='IGI')
    value_added_tax = fields.Monetary(string='IVA')
    customs_processing_right = fields.Monetary(string='DTA')
    prevalidation = fields.Monetary(string='PRV')
    vat_prevalidation = fields.Monetary(string='IVA / PRV')
    customs_charges = fields.Monetary(string='Gastos en aduana')
    storages = fields.Monetary(string='Almacenajes')
    delays = fields.Monetary(string='Demoras')
    land_freight = fields.Monetary(string='Flete terrestre')
    salary_customs_agents = fields.Monetary(string='Honorarios Agente Aduanal')