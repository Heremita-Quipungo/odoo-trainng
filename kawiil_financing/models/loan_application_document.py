from odoo import fields, models


class LoanApplicationDocument(models.Model):
    _name = 'loan.application.document'
    _description = 'Loan Application Document'
    _order = 'id desc'

    name = fields.Char(string='Document Name', required=True)

    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        string='Status',
        default='new',
        required=True,
    )

    type_id = fields.Many2one(
        comodel_name='loan.application.document.type',
        string='Document Type',
        ondelete='restrict',
    )

    application_id = fields.Many2one(
        comodel_name='loan.application',
        string='Loan Application',
        ondelete='cascade',
        required=True,
    )

    attachment_id = fields.Many2one(
        comodel_name='ir.attachment',
        string='Attachment',
        ondelete='set null',
    )