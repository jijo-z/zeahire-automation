from playwright.sync_api import expect
from pages.base_page import BasePage
from config.config import BASE_URL
from pages.settings_page import SettingsPage
from pages.how_it_works_page import HowItWorksPage



class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.url = f"{BASE_URL}/dashboard"

        # ===== Header =====
        self.hiring_statistics_title = page.get_by_role(
            "heading", name="Hiring Statistics"
        )
        self.new_job_btn = page.locator("a[href='/jobs/create']")
        self.notifications_btn = page.locator(
            "button"
        ).filter(has=page.locator("img[alt='Notifications']"))
        self.profile_section = page.locator("button[id^='radix-']")

        # ===== Top Widgets (stable locators) =====
        self.candidates_card = page.locator("text=Candidates").first
        self.active_jobs_card = page.locator("text=Active Jobs").first
        self.interviews_completed_card = page.locator("text=Interviews Completed").first
        self.hiring_rate_card = page.locator("text=Hiring Rate").first
        self.rejected_candidates_card = page.locator("text=Rejected Candidates").first

        # ===== Charts =====
        self.applications_chart = page.locator("text=Applications").first
        self.department_chart = page.locator("text=Application by Department").first

        # ===== Tabs & Table =====
        self.recent_applications_tab = page.get_by_role(
            "button", name="Recent Applications"
        )
        self.recent_jobs_tab = page.get_by_role(
            "button", name="Recent Jobs"
        )
        self.table = page.locator("table").first

        # ===== Right Widgets =====
        self.interview_calendar = page.locator("text=Interview Calendar").first
        self.hiring_pipeline = page.locator("text=Hiring Pipeline").first

    # ================= ACTIONS ================= #
    def open(self):
        self.page.goto(self.url, wait_until="networkidle")
        self.hiring_statistics_title.wait_for(state="visible", timeout=20000)

    # ================= ASSERTIONS ================= #
    def verify_header(self):
        expect(self.hiring_statistics_title).to_be_visible(timeout=20000)
        expect(self.new_job_btn).to_be_visible()
        expect(self.notifications_btn).to_be_visible()
        expect(self.profile_section).to_be_visible()

    def verify_top_widgets(self):
        expect(self.candidates_card).to_be_visible(timeout=20000)
        expect(self.active_jobs_card).to_be_visible()
        expect(self.interviews_completed_card).to_be_visible()
        expect(self.hiring_rate_card).to_be_visible()
        expect(self.rejected_candidates_card).to_be_visible()

    def verify_charts(self):
        expect(self.applications_chart).to_be_visible(timeout=20000)
        expect(self.department_chart).to_be_visible()

    def verify_tabs_and_table(self):
        expect(self.recent_applications_tab).to_be_visible(timeout=20000)
        expect(self.recent_jobs_tab).to_be_visible()
        expect(self.table).to_be_visible()

    def verify_right_widgets(self):
        expect(self.interview_calendar).to_be_visible(timeout=20000)
        expect(self.hiring_pipeline).to_be_visible()

    def verify_all_elements_visible(self):
        self.verify_header()
        self.verify_top_widgets()
        self.verify_charts()
        self.verify_tabs_and_table()
        self.verify_right_widgets()
        
    def go_to_settings(self):
        self.page.get_by_role("link", name="Settings").click()
        return SettingsPage(self.page)    
    


    def go_to_how_it_works(self):
        self.page.goto("https://qa.zeahire.ai/how-it-works")
        return HowItWorksPage(self.page)
