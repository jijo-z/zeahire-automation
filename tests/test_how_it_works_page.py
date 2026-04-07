import pytest
from pages.how_it_works_page import HowItWorksPage


@pytest.mark.smoke
def test_how_it_works_page_load(dashboard_page):
    dashboard = dashboard_page

    # Navigate (you must add this in dashboard)
    how_page = dashboard.go_to_how_it_works()

    assert how_page.is_loaded(), "How It Works page failed to load"