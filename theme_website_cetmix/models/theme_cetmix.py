from odoo import models


class ThemeWebsiteCetmix(models.AbstractModel):
    _inherit = "theme.utils"

    def _theme_website_cetmix_post_copy(self, mod):
        self.enable_view("website.template_header_centered_logo")
        self.enable_view("theme_website_cetmix.template_cx_call_to_action_custom")
        self.enable_view("theme_website_cetmix.template_cx_custom_footer")
        self.enable_view("theme_website_cetmix.template_cx_footer_company_name")
        self.enable_view("theme_website_cetmix.template_cx_contact_us")
        menu = self.env.ref("website.menu_contactus", raise_if_not_found=False)
        if menu:
            menu.unlink()
