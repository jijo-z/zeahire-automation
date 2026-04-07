from playwright.sync_api import expect
from pages.base_page import BasePage
from config.config import BASE_URL


class CreateJobPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # ===== URL =====
        self.url = f"{BASE_URL}/jobs/create"

        # ===== PAGE 1 =====
        self.job_title_input = page.locator("input[name='title']")
        self.next_btn = page.get_by_role("button", name="Next")

        # Comboboxes
        self.comboboxes = page.locator("button[role='combobox']")

        # AI Generate buttons (global)
        self.ai_generate_buttons = page.locator("button:has-text('AI Generate')")

        # ===== PAGE 2 =====
        self.min_exp_input = page.locator("input[name='minimum_experience_years']")
        self.education_input = page.locator("input[name='required_education']")

        # ===== PAGE 3 =====
        self.state_input = page.locator("input[name='state']")
        self.city_input = page.locator("input[name='city']")

        # ===== FINAL =====
        self.create_btn = page.get_by_role("button", name="Create Job")

        # Toast
        self.success_toast = page.locator(
            "li[role='status']",
            has_text="Job Created Successfully"
        )

    # ======================================================
    # OPEN PAGE
    # ======================================================
    def open(self):
        self.page.goto(self.url, wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")

    # ======================================================
    # PAGE 1 — BASIC DETAILS
    # ======================================================
    def fill_basic_details(self, job_title: str):
        expect(self.job_title_input).to_be_visible(timeout=20000)
        self.job_title_input.fill(job_title)

        # Department
        self.comboboxes.nth(0).click()
        dept = self.page.locator("div[role='option']").filter(has_text="Quality Assurance").first
        expect(dept).to_be_visible(timeout=20000)
        dept.click()

        # Employment Type
        self.comboboxes.nth(1).click()
        emp = self.page.locator("div[role='option']").filter(has_text="Full Time").first
        expect(emp).to_be_visible(timeout=20000)
        emp.click()

        # Experience Level
        self.comboboxes.nth(2).click()
        exp = self.page.locator("div[role='option']").filter(has_text="Mid Level").first
        expect(exp).to_be_visible(timeout=20000)
        exp.click()

        # AI Generate Job Description
        expect(self.ai_generate_buttons.first).to_be_visible(timeout=20000)
        self.ai_generate_buttons.first.click()
        self.page.wait_for_timeout(3000)

        # AI Generate Short Description
        self.ai_generate_buttons.nth(1).click()
        self.page.wait_for_timeout(3000)

        self.next_btn.click()

    # ======================================================
    # PAGE 2 — INFORMATION
    # ======================================================
    def fill_information_page(self):
        expect(self.min_exp_input).to_be_visible(timeout=20000)
        self.min_exp_input.fill("3")
        self.education_input.fill("Bachelor's Degree")

        # AI Generate Required Skills
        self.ai_generate_buttons.nth(0).click()
        self.page.wait_for_timeout(3000)

        # AI Generate Preferred Skills
        self.ai_generate_buttons.nth(1).click()
        self.page.wait_for_timeout(3000)

        self.next_btn.click()

    # ======================================================
    # PAGE 3 — LOCATION
    # ======================================================
    def fill_location_page(self):
        # Use label anchor for stable country dropdown
        country_label = self.page.get_by_text("Country", exact=True)
        expect(country_label).to_be_visible(timeout=20000)

        country_dropdown = country_label.locator(
            "xpath=following::button[@role='combobox'][1]"
        )
        country_dropdown.click()

        india = self.page.locator("div[role='option']").filter(has_text="India").first
        expect(india).to_be_visible(timeout=20000)
        india.click()

        expect(self.state_input).to_be_visible(timeout=20000)
        self.state_input.fill("Karnataka")
        self.city_input.fill("Bangalore")
        
        self.next_btn.click()
    # ======================================================
    # FINAL SUBMIT
    # ======================================================
    def create_job(self):
        self.create_btn.scroll_into_view_if_needed()
        expect(self.create_btn).to_be_enabled(timeout=20000)
        self.create_btn.click()

    # ======================================================
    # ASSERTION
    # ======================================================
    def assert_job_created(self):
        self.success_toast.wait_for(state="visible", timeout=20000)
        expect(self.success_toast).to_be_visible()