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
        "website",
        "web_unsplash",
        'website_profile',
    ],
    'external_dependencies': {},
    "data": [
        #"views/cx_header_logo.xml",
        "views/cx_header.xml",
        "views/cx_homepage.xml",
    ],
    "assets": {
        'web.assets_frontend': [
            "cx_website_cetmix/static/src/scss/user_values.scss",
            #"cx_website_cetmix/static/src/scss/colors/user_color_palette.scss",
            #"cx_website_cetmix/static/src/scss/colors/user_theme_color_palette.scss",
        ],
    },
    "qweb": [],
    "installable": True,
    "application": True,
}
