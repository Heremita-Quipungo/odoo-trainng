from odoo import fields, models


class LoanApplication(models.Model):
    _name = 'loan.application'
    _description = 'Loan Application'

    name = fields.Char(
        string="Application Reference",
        required=True,
        copy=True,
    )
    loan_amount = fields.Monetary(
        string="Loan Amount",
        currency_field="currency_id",
        required=True,
    )

    interest_rate = fields.Float(
        string="Interest Rate",
        digits=(5, 2),
        required=True,
    )

    loan_term = fields.Integer(
        string="Loan Term (Months)",
        default=36,
    )

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("sent", "Submitted"),
            ("credit_check", "Credit Check"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
            ("signed", "Signed"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        default="draft",
        copy=False,
    )

    notes = fields.Html(
        string="Notes",
        copy=False,
    )
    date_applied = fields.Date(
        string='Application Date', default=fields.Date.today,
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        required=True,
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Salesperson',
        default=lambda self: self.env.user,
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Motorcycle',
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )
    down_payment = fields.Monetary(
        string='Down Payment',
        currency_field='currency_id',
    )
    active = fields.Boolean(
        string="Active",
        default=True,
        copy=False,
    )
    tag_ids = fields.Many2many(
        comodel_name='loan.application.tag',
        relation='loan_application_tag_rel',
        column1='application_id',
        column2='tag_id',
        string='Tags',
    )

    document_ids = fields.One2many(
        comodel_name='loan.application.document',
        inverse_name='application_id',
        string='Documents',
    )
