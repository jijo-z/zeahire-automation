import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_jobs_page_load(dashboard_page):
    """
    Validate Jobs page loads and key components are visible
    """

    dashboard = dashboard_page
    page = dashboard.page

    # Open Jobs page
    page.goto("https://qa.zeahire.ai/jobs")

    # ===== PAGE TITLE =====
    expect(page.get_by_role("heading", name="Jobs")).to_be_visible()

    # ===== JOB TABLE =====
    expect(page.locator("tbody tr").first).to_be_visible()

    # ===== JOB LINK =====
    expect(page.locator("a[href^='/jobs/']").first).to_be_visible()

    # ===== VIEW BUTTON =====
    expect(page.locator("a[title='View']").first).to_be_visible()

    # ===== EDIT BUTTON =====
    expect(page.locator("button[title='Edit']").first).to_be_visible()

    # ===== ACTION MENU =====
    expect(page.locator("button[aria-haspopup='menu']").first).to_be_visible()