{
    "name": "Cetmix Website New",
    "version": "16.0.0.1.0",
    "summary": "Cetmix Website Odoo 16 Module",
    "author": "Cetmix",
    "license": "LGPL-3",
    "category": "Theme/Cetmix",
    "website": "https://cetmix.com",
    "live_test_url": "https://demo.cetmix.com",
    "depends": [
        "website",
    ],
    "external_dependencies": {},
    "data": [
        "data/data.xml",
        "views/cx_header.xml",
        #"views/cx_cetmix.xml",
        "views/cx_homepage.xml",
    ],
    "assets": {
        "web._assets_primary_variables": [
            "theme_website_cetmix/static/src/scss/options/user_values.scss",
            "theme_website_cetmix/static/src/scss/options/colors/user_color_palette.scss",
            "theme_website_cetmix/static/src/scss/options/colors/user_theme_color_palette.scss",
        ],
    },
    "qweb": [],
    "installable": True,
    "application": True,
}