# -*- coding: utf-8 -*-
from odoo import http

# class WbProductImport(http.Controller):
#     @http.route('/wb_product_import/wb_product_import/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wb_product_import/wb_product_import/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wb_product_import.listing', {
#             'root': '/wb_product_import/wb_product_import',
#             'objects': http.request.env['wb_product_import.wb_product_import'].search([]),
#         })

#     @http.route('/wb_product_import/wb_product_import/objects/<model("wb_product_import.wb_product_import"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wb_product_import.object', {
#             'object': obj
#         })