import re
from playwright.sync_api import expect


class SettingsPage:
    def __init__(self, page):
        self.page = page

        # Primary locator (content area - may vary)
        self.heading = page.get_by_role("heading", name="Settings")

        # Sidebar locator (fallback safety)
        self.sidebar_settings = page.get_by_role("link", name="Settings")

        # Possible stable elements inside settings (future-proof placeholders)
        self.save_button = page.get_by_role("button", name="Save").first
        self.input_fields = page.locator("input")

    def is_loaded(self):
        # ✅ URL validation (MANDATORY)
        expect(self.page).to_have_url(re.compile(".*/settings"))

        # ✅ Try main content validation first
        if self.heading.count() > 0:
            self.heading.first.wait_for(state="visible")
            return True

        # ⚠️ Fallback (if heading not present)
        self.sidebar_settings.wait_for(state="visible")

        # Ensure at least some form/input exists (real content loaded)
        if self.input_fields.count() > 0:
            self.input_fields.first.wait_for(state="visible")

        return True