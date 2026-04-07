import pytest
from pages.dashboard_page import DashboardPage


@pytest.mark.smoke
def test_dashboard_elements_visibility(dashboard_page):
    dashboard = dashboard_page
    page = dashboard.page
    dashboard = DashboardPage(page)

    dashboard.open()
    dashboard.verify_all_elements_visible()
