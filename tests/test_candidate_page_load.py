import pytest
import re
from playwright.sync_api import expect

from conftest import page



@pytest.mark.smoke
def test_candidates_page_load(dashboard_page):
    dashboard = dashboard_page
    page = dashboard.page

    page.goto("https://qa.zeahire.ai/candidates")

    page.get_by_role("heading", name="Candidates").first.wait_for()

    