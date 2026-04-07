import pytest
from pages.settings_page import SettingsPage


@pytest.mark.smoke
def test_settings_page_load(dashboard_page):
    dashboard = dashboard_page

    # Navigate to settings
    # test
    settings_page = dashboard.go_to_settings()

    # Validate page load
    assert settings_page.is_loaded(), "Settings page failed to load"