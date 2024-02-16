# -*- coding: utf-8 -*-
# from odoo import http


# class Hospital-tareaTres(http.Controller):
#     @http.route('/hospital-tarea_tres/hospital-tarea_tres', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital-tarea_tres/hospital-tarea_tres/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital-tarea_tres.listing', {
#             'root': '/hospital-tarea_tres/hospital-tarea_tres',
#             'objects': http.request.env['hospital-tarea_tres.hospital-tarea_tres'].search([]),
#         })

#     @http.route('/hospital-tarea_tres/hospital-tarea_tres/objects/<model("hospital-tarea_tres.hospital-tarea_tres"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital-tarea_tres.object', {
#             'object': obj
#         })

