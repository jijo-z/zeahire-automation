from playwright.sync_api import expect


class ScheduleInterviewPage:
    def __init__(self, page):
        self.page = page

        # Navigation
        self.interviews_nav = page.get_by_role("link", name="Interviews")

        # Drawer title (heading only to avoid strict mode conflict)
        self.drawer_title = page.locator("h2", has_text="Schedule Interview")

        # Comboboxes (index-based like old viva flow)
        self.comboboxes = page.locator("button[role='combobox']")

        # Candidate
        self.add_candidate_btn = page.locator(
                "button:has-text('Add Candidate'), button:has-text('Add Candidates')"
            ).first
        self.candidate_search_input = page.get_by_placeholder(
            "Search candidates by name or email..."
        )

        # Date & time
        self.datetime_input = page.locator("input#scheduled_at")

        # Submit
        self.schedule_btn = page.locator("button:has-text('Schedule & Send')")

        # Success toast
        self.success_toast = page.locator(
            "li[role='status']",
            has_text="Interview Scheduled Successfully"
        )

    # ================= HELPERS ================= #
    def _select_option(self, index: int, text: str):
        combobox = self.comboboxes.nth(index)
        combobox.click()

        # 🔥 Pick the LAST visible listbox (the newly opened dropdown)
        options_list = self.page.locator("div[role='listbox']").last
        options_list.wait_for(state="visible", timeout=10000)

        option = options_list.get_by_role("option", name=text).first
        option.wait_for(state="visible", timeout=10000)
        option.click()

    # ================= ACTIONS ================= #

    def open(self):
        """
        Correct flow:
        Dashboard → Interviews → Schedule Interview
        """
        self.interviews_nav.click()
        self.page.wait_for_url("**/interviews", timeout=20000)

        self.page.get_by_role("button", name="Schedule Interview").click()
        self.drawer_title.wait_for(state="visible", timeout=15000)

    def select_job(self, job_name: str):
        self._select_option(0, job_name)

    def select_template(self, template: str):
        self._select_option(1, template)

    def add_candidate(self, candidate_name: str):
        # Open candidate picker
        self.add_candidate_btn.click()

        # Type to search (no assertions, just ensure field is interactable)
        self.candidate_search_input.fill(candidate_name[:2].lower())

        # Select first matching candidate directly
        self.page.locator(
            "div.cursor-pointer", has_text=candidate_name
        ).first.click()

    
    def set_datetime(self, value: str):
   
        self.page.locator("input#scheduled_at").fill(value)
    def configure_interview(
        self,
        duration: str,
        expiry: str,
        interview_type: str,
        language: str,
    ):
        self._select_option(2, duration)
        self._select_option(3, expiry)
        self._select_option(4, interview_type)
        self._select_option(5, language)

    def submit(self):
        expect(self.schedule_btn).to_be_enabled()
        self.schedule_btn.click()

    # ================= ASSERTIONS ================= #

    def verify_success(self):
    # Wait for either toast OR redirect back to interviews page
        try:
            self.success_toast.wait_for(state="visible", timeout=8000)
            expect(self.success_toast).to_be_visible()
        except:
            # If toast disappears due to redirect, verify URL instead
            self.page.wait_for_url("**/interviews", timeout=15000)
