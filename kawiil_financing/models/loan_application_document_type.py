from odoo import fields, models


class LoanApplicationDocumentType(models.Model):
    _name = 'loan.application.document.type'
    _description = 'Loan Application Document Type'
    _order = 'name'

    name = fields.Char(string='Document Type', required=True)
    is_required = fields.Boolean(string='Required', default=False)
    active = fields.Boolean(string='Active', default=True)