import pytest


@pytest.mark.smoke
def test_schedule_page_load(dashboard_page):

    dashboard = dashboard_page
    page = dashboard.page

    # open schedule page
    page.goto(
        "https://qa.zeahire.ai/schedule",
        wait_until="domcontentloaded"
    )

    # ===== Page title =====
    page.get_by_role("heading", name="Schedule").first.wait_for()

    # ===== Calendar tab =====
    assert page.locator("role=tab[name='Calendar']").is_visible()

    # ===== Upcoming tab =====
    assert page.locator("role=tab[name='Upcoming']").is_visible()

    # ===== Today button =====
    assert page.locator("button:has-text('Today')").is_visible()

    # ===== Today's Interview Schedule section =====
    assert page.locator("text=Today's Interview Schedule").is_visible()

    # ===== Sidebar navigation validation =====
    page.get_by_role("link", name="Dashboard").first.wait_for()
    page.get_by_role("link", name="Jobs").first.wait_for()
    page.get_by_role("link", name="Candidates").first.wait_for()
    page.get_by_role("link", name="Interviews").first.wait_for()
    page.get_by_role("link", name="Schedule").first.wait_for()
    page.get_by_role("link", name="Insights").first.wait_for()
    