from playwright.sync_api import Page, expect


class ResumeParsingPage:
    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.candidates_tab = page.get_by_role("link", name="Candidates")
        self.add_candidate_btn = page.get_by_role("button", name="Add Candidate")

        # Job dropdown (combobox)
        self.job_combobox = page.get_by_role("combobox").first

        # Upload tab & input
        self.upload_tabpanel = page.get_by_role("tabpanel", name="Upload Resume")
        self.file_input = self.upload_tabpanel.locator("input[type='file']").first

        # Upload & Parse button (note: UI shows "Upload and Parse")
        self.upload_parse_btn = page.get_by_role("button", name="Upload and Parse")
        # Generic toast
        self.success_toast = page.locator("div[role='status'], li[role='status']").first

    # -------------------------------------------------
    # COMMON WAIT
    # -------------------------------------------------
    def _wait_for_ui(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)

    # -------------------------------------------------
    # NAVIGATION
    # -------------------------------------------------
    def open_candidates_page(self):
        self.candidates_tab.click()
        expect(self.add_candidate_btn).to_be_visible(timeout=20000)

    def open_add_candidate(self):
        self._wait_for_ui()
        self.add_candidate_btn.click()

        # Wait until job combobox is visible (drawer opened)
        expect(self.job_combobox).to_be_visible(timeout=20000)

    # -------------------------------------------------
    # JOB SELECTION
    # -------------------------------------------------
    def associate_job(self, job_name: str):
        self._wait_for_ui()

        self.job_combobox.click()

        option = self.page.get_by_role("option", name=job_name)
        option.wait_for(state="visible", timeout=20000)
        option.click()

    # -------------------------------------------------
    # FILE UPLOAD
    # -------------------------------------------------
    def upload_resumes(self, file_paths: list[str]):
        expect(self.file_input).to_be_attached(timeout=20000)
        self.file_input.set_input_files(file_paths)

    # -------------------------------------------------
    # UPLOAD & PARSE (CLICK IMMEDIATELY AFTER UPLOAD)
    # -------------------------------------------------
    def upload_and_parse(self):
        self._wait_for_ui()

        # Do NOT wait for assertions; click as soon as visible
        self.upload_parse_btn.wait_for(state="attached", timeout=20000)
        self.upload_parse_btn.click(force=True)

        # Backend processing buffer
        self.page.wait_for_timeout(5000)

    # -------------------------------------------------
    # SUCCESS ASSERTION
    # -------------------------------------------------
    def assert_upload_success(self):
        self.success_toast.wait_for(state="visible", timeout=20000)