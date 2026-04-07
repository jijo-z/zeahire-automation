import time
from playwright.sync_api import expect


class InterviewTemplatePage:
    def __init__(self, page):
        self.page = page

        # ================= NAVIGATION =================
        self.interviews_nav = page.get_by_role("link", name="Interviews")
        self.templates_nav = page.get_by_role("link", name="Templates")

        self.create_template_btn = page.get_by_role(
            "button", name="Create Template"
        )
        self.create_from_scratch_btn = page.get_by_role(
            "button", name="Create from Scratch"
        )

        # ================= FORM / DRAWER =================
        self.drawer = page.locator("form#template-form")
        self.name_input = page.locator("input#name")
        self.instructions_input = page.locator("textarea#instructions")

        # ================= DROPDOWNS =================
        self.round_dropdown = page.get_by_role("combobox").nth(0)
        self.language_dropdown = page.get_by_role("combobox").nth(1)

        # ================= QUESTIONS =================
        self.add_question_btn = page.locator(
            "button:has-text('Add Question')"
        )
        self.ai_generate_btn = page.locator(
            "button:has-text('AI Generate')"
        )

        # ================= SUBMIT =================
        self.submit_btn = page.locator(
            "button[type='submit'][form='template-form']"
        )

        # ================= TOASTS =================
        self.ai_generated_toast = page.locator(
            "li[role='status']", has_text="AI Content Generated"
        )
        self.success_toast = page.locator(
            "li[role='status']", has_text="Template Created"
        )

        # overlay blocker
        self.overlay = page.locator("div.fixed.z-50")

    # ================= HELPERS =================

    def _wait_for_ui(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1500)

        try:
            if self.overlay.is_visible():
                self.overlay.wait_for(state="hidden", timeout=15000)
        except:
            pass

    def _select_dropdown_option(self, dropdown, text):
        dropdown.click()
        option = self.page.locator(
            "div[role='option']", has_text=text
        ).first
        option.wait_for(state="visible", timeout=15000)
        option.click()

    # ================= FLOW =================

    def open(self):
        """Dashboard → Interviews → Create Template → Create from Scratch"""
        self._wait_for_ui()

        # Step 1: Go to Interviews
        expect(self.interviews_nav).to_be_visible(timeout=20000)
        self.interviews_nav.click()
        self.page.wait_for_url("**/interviews", timeout=20000)

        # Step 2: Click 'Create Template' directly (no Templates tab anymore)
        expect(self.create_template_btn).to_be_visible(timeout=20000)
        self.create_template_btn.click()

        # Step 3: Click Create from Scratch
        expect(self.create_from_scratch_btn).to_be_visible(timeout=20000)
        self.create_from_scratch_btn.click()

        # Step 4: Wait for drawer
        self.drawer.wait_for(state="visible", timeout=20000)

    # ================= BASIC INFO =================

    def enter_template_name(self, name: str):
        expect(self.name_input).to_be_visible(timeout=20000)
        self.name_input.fill(name)

    def select_interview_round(self, round_name: str):
        self._select_dropdown_option(self.round_dropdown, round_name)

    def select_language(self, language: str):
        self._select_dropdown_option(self.language_dropdown, language)

    # ================= QUESTIONS =================

    def add_questions(self, count: int = 15):
        for _ in range(count):
            self.add_question_btn.click()

    def ai_generate_questions(self, count_text="15 Questions"):
        self._wait_for_ui()

        self.ai_generate_btn.first.click()

        dialog = self.page.locator("div[role='dialog']").first
        dialog.wait_for(state="visible", timeout=20000)

        # Select number of questions (2nd dropdown inside dialog)
        dropdown = dialog.locator("button[role='combobox']").nth(1)
        dropdown.click()

        option = self.page.locator(
            "div[role='option']", has_text=count_text
        ).first
        option.wait_for(state="visible", timeout=15000)
        option.click()

        dialog.locator(
            "button:has-text('Generate Content')"
        ).click()

        # Wait for AI toast
        self.ai_generated_toast.wait_for(
            state="visible", timeout=20000
        )

        self.page.wait_for_load_state("networkidle")
        # wait for AI processing
        self.page.wait_for_timeout(5000)

        # optional check (safe)
        if self.page.get_by_placeholder("Enter the Interview question").count() > 0:
         self.page.get_by_placeholder("Enter the Interview question").first.wait_for()

        # Close dialog
        self.page.keyboard.press("Escape")
        self.page.wait_for_timeout(1000)

    # ================= SAVE TEMPLATE =================

    def save_template(self):
        # Scroll to button
        self.submit_btn.scroll_into_view_if_needed()

        # Wait until enabled
        expect(self.submit_btn).to_be_enabled(timeout=20000)

        # Wait for animations to settle
        self.page.wait_for_timeout(1000)

        # Click with force (drawer overlay safe)
        self.submit_btn.click(force=True)



    # ================= ASSERTIONS =================

    def assert_template_created(self):
        # First try toast
        try:
            self.success_toast.wait_for(state="visible", timeout=15000)
            expect(self.success_toast).to_be_visible()
            return
        except:
            pass

        # Fallback: drawer closes after submit
        self.drawer.wait_for(state="hidden", timeout=15000)