import pytest


@pytest.mark.smoke
def test_team_management_page_load(dashboard_page):

    page = dashboard_page.page

    page.goto(
        "https://qa.zeahire.ai/dashboard/team",
        wait_until="domcontentloaded"
    )

    # ✅ Page loaded (sidebar present)
    page.get_by_role("link", name="Dashboard").first.wait_for()

    # ✅ Team page is active (from sidebar)
    page.get_by_role("link", name="Team Management").first.wait_for()