{
    "name": "Cetmix Website New",
    "version": "16.0.0.1.0",
    "summary": "Cetmix Website Odoo 16 Module",
    "author": "Cetmix",
    "license": "LGPL-3",
    "category": "Theme/Cetmix",
    'website': 'https://cetmix.com',
    'live_test_url': 'https://demo.cetmix.com',
    "depends": [
        "base",
        "mail",
        "website",
        "web_unsplash",
        'website_profile',
    ],
    'external_dependencies': {
    },
    "data": [
        'data/ir_asset.xml',
        "views/cx_header.xml",
        "views/cx_homepage.xml",
    ],
    "qweb": [],
    "installable": True,
    "application": True,
}
