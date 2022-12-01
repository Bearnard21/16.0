from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)


class CetmixWebsiteTemplate(http.Controller):
    @http.route("/cetmix/home", type="http", auth="public", website=True)
    def cetmix_website_template(self):
        return http.request.render('website.homepage')
