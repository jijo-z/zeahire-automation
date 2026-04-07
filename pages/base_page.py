from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # ---------- Common Actions ---------- #
    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def type(self, locator, text):
        self.page.locator(locator).type(text)

    def wait_visible(self, locator, timeout=20000):
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def expect_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def expect_text(self, locator, text):
        expect(self.page.locator(locator)).to_contain_text(text)