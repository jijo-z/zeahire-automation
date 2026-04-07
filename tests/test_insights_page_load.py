import pytest


@pytest.mark.smoke
def test_insights_page_load(dashboard_page):

    dashboard = dashboard_page
    page = dashboard.page

    # open insights page
    page.goto(
        "https://qa.zeahire.ai/insights",
        wait_until="domcontentloaded"
    )

    # wait for react render
    page.get_by_role("heading", name="Insights").first.wait_for()

    