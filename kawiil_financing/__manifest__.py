{
    "name": "Kawiil Financing",
    "version": "1.0.1",
    "category": "Kawiil/Custom Modules",
    "summary": "Streamlines the loan application process for dealerships.",
    "author": "ODOP Trainee",
    "maintainer": "José M. Quipungo",  # TODO: replace with your full name
    "website": "https://github.com/odoo-trainings/kawiil-motors/",
    "license": "OPL-1",
    "depends": ["product"],
    'data': [
            # Security
        'security/kawiil_financing_groups.xml',
        'security/kawiil_financing_security.xml',
        'security/ir.access.csv',
            # Views
        'views/loan_application_views.xml',
        'views/kawiil_financing_menu.xml',
        'views/loan_application_form_compliance.xml',
        'views/loan_application_tag_config_views.xml',

    ],
    "demo": [
        'demo/loan_demo.xml',
        'demo/config_demo.xml'
    ],
    "application": True,
}
