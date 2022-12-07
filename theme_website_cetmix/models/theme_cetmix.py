from odoo import models


class ThemeWebsiteCetmix(models.AbstractModel):
    _inherit = "theme.utils"

    def _theme_website_cetmix_post_copy(self, mod):
        self.enable_view("website.template_header_centered_logo")
        self.enable_view("website.template_footer_centered")

        # self.enable_view('website.template_footer_contact')
