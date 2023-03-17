from odoo import http,_
from ..models.token_create import TokenCreate

class CustomerQueue(http.Controller):

    @http.route('/token/generate/', website=True ,auth='public')
    def index(self, **kw):
        dep = http.request.env['hr.department']
        if 'customer_name' in kw and 'service' in kw and kw['customer_name'] !="":
            vals = {'name': _('New'), 'customer_name': kw['customer_name'] , 'customer_mobile': kw['phone_no'] , 'department': kw['department'], 'service_done': True if kw['service'] == 'on' else False  }
            token_gen = http.request.env['token.token'].sudo().create(vals)
        return http.request.render("customer_queue.web_customer_queue",{
            "department": dep.search([])
        })
    @http.route('/token/service/', website=True ,auth='public')
    def customer_service(self, **kw):

        return http.request.render("customer_queue.web_customer_queue",{})