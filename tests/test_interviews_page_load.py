import pytest

from conftest import page


@pytest.mark.smoke
def test_interviews_page_load(dashboard_page):
    """
    Smoke test:
    Verify Interviews page loads and main components are visible
    """

    dashboard = dashboard_page
    page = dashboard.page

    # ===== Open Interviews page =====
    page.goto(
        "https://qa.zeahire.ai/interviews",
        wait_until="domcontentloaded"
    )

    # ===== Page title =====
    page.get_by_role("heading", name="Interviews").first.wait_for()

    # ===== Header buttons =====
    refresh_button = page.locator("text=Refresh").first
    assert refresh_button.is_visible()

    auto_refresh_toggle = page.locator("text=Auto-refresh").first
    assert auto_refresh_toggle.is_visible()

    # ===== Statistics cards =====
    total_interviews_card = page.locator("text=Total Interviews").first
    assert total_interviews_card.is_visible()

    total_candidates_card = page.locator("text=Total Candidates").first
    assert total_candidates_card.is_visible()

    # ===== Sidebar navigation validation =====
    page.get_by_role("link", name="Dashboard").first.wait_for()
    page.get_by_role("link", name="Jobs").first.wait_for()
    page.get_by_role("link", name="Candidates").first.wait_for()
    page.get_by_role("link", name="Interviews").first.wait_for()
    page.get_by_role("link", name="Schedule").first.wait_for()
    page.get_by_role("link", name="Insights").first.wait_for()