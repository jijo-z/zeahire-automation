from playwright.sync_api import expect
from pages.base_page import BasePage
from config.config import BASE_URL


class TeamManagementPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.url = f"{BASE_URL}/dashboard/team"

        # Buttons
        self.add_user_btn = page.get_by_role("button", name="Add User")

        # Will be scoped after dialog opens
        self.dialog = None

        # Toast
        self.success_toast = page.locator(
            "li[role='status']",
            has_text="User"
        )

    # ================= ACTIONS ================= #

    def open(self):
        self.page.goto(self.url, wait_until="domcontentloaded")

    def open_add_member_dialog(self):
        self.page.get_by_role("button", name="Add User").click()

        # wait for dialog to open
        self.dialog = self.page.locator("div[role='dialog']")
        self.dialog.wait_for(state="visible", timeout=10000)
    def fill_basic_info(self, email, password, first, last, phone):

        dialog = self.page.locator("div[role='dialog']")
        dialog.wait_for(state="visible")

        dialog.locator("#org-create-user-email").fill(email)
        dialog.locator("#password").fill(password)
        dialog.locator("#first_name").fill(first)
        dialog.locator("#last_name").fill(last)
        dialog.locator("#phone").fill(phone)
    
    def select_role(self, role="Recruiter"):
        dialog = self.page.locator("div[role='dialog']")

        role_dropdown = dialog.locator("button[role='combobox']").nth(0)
        role_dropdown.click()

        option = self.page.locator("div[role='option']", has_text=role)
        option.first.click()

    def select_first_timezone(self):
        timezone_dropdown = self.dialog.locator("button[role='combobox']").nth(1)
        timezone_dropdown.click()

        option = self.page.locator(
            "div[role='option']:not([aria-disabled='true'])"
        ).first
        option.wait_for(state="visible", timeout=10000)
        option.click()

    def submit(self):
        dialog = self.page.locator("div[role='dialog']")

        add_btn = dialog.locator("button:has-text('Add Team Member')")
        add_btn.click()

    # ================= ASSERTIONS ================= #

    def assert_member_added(self):
        self.success_toast.wait_for(state="visible", timeout=20000)
        expect(self.success_toast).to_contain_text("User")