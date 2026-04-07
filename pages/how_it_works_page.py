import re
from playwright.sync_api import expect


class HowItWorksPage:
    def __init__(self, page):
        self.page = page

        # 🔥 Primary unique heading (VERY STRONG)
        self.main_heading = page.get_by_role(
            "heading", name="How ZeaHire Transforms Hiring"
        )

        # 🔥 Section heading (secondary validation)
        self.process_heading = page.get_by_role(
            "heading", name="Complete Process Overview"
        )

        # 🔥 CTA button
        self.try_button = page.get_by_role("link", name="Try ZeaHire Now")

        # 🔥 Workflow section anchor
        self.workflow_section = page.locator("#workflow")

    def is_loaded(self):
        # ✅ URL validation
        expect(self.page).to_have_url(re.compile(".*how-it-works"))

        # ✅ Main heading
        self.main_heading.wait_for(state="visible")

        # ✅ Secondary validation
        self.process_heading.wait_for(state="visible")

        # ✅ CTA validation
        self.try_button.wait_for(state="visible")

        return True