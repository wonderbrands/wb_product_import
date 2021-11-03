# -*- coding: utf-8 -*-
{
    'name': "Import Product Fields",

    'summary': """
        New fields in product template to importation tracking """,

    'description': """
    Se agregan campos necesarios para el seguimiento de valores que definen el precio total del producto importado:
        Fracción arancelaria
Porcentaje de arancel
NOM
Flete
IGI
IVA
DTA
PRV
IVA / PRV
Gastos en aduana
Almacenajes
Demoras
Flete terrestre
Honorarios Agente Aduanal
    """,

    'author': "Wonder Brands",
    'website': "http://www.wonderbrands.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}