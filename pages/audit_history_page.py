class AuditHistoryPage:

    def __init__(self, page):
        self.page = page

        # Title
        self.title = page.get_by_text("Organization Audit History")

        # Buttons
        self.refresh_button = page.get_by_role("button", name="Refresh")
        self.export_button = page.get_by_role("button", name="Export CSV")
        self.reset_button = page.get_by_role("button", name="Reset")

        # Filters
        self.event_filter = page.get_by_role("combobox").nth(1)
        self.tier_filter = page.get_by_role("combobox").nth(2)
        self.search_input = page.get_by_placeholder("Search event message...")

        # Empty state
        self.empty_message = page.get_by_text("No audit events found")

    def validate_page_loaded(self):
        self.title.wait_for()
        assert self.title.is_visible()

    def validate_components_loaded(self):
        self.refresh_button.wait_for()
        self.export_button.wait_for()
        self.search_input.wait_for()

        assert self.refresh_button.is_visible()
        assert self.export_button.is_visible()
        assert self.search_input.is_visible()