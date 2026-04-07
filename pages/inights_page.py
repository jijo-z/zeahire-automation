import pytest


@pytest.mark.smoke
def test_insights_page_load(dashboard_page):

    page = dashboard_page

    # open insights page
    page.goto(
        "https://qa.zeahire.ai/insights",
        wait_until="domcontentloaded"
    )

    # ===== Page title =====
    assert page.locator("h1:has-text('Insights')").first.is_visible()

    # ===== Export button =====
    assert page.locator("button:has-text('Export Data')").is_visible()

    # ===== Main widgets =====
    assert page.locator("text=Recruitment Efficiency").is_visible()
    assert page.locator("text=Candidate Experience").is_visible()
    assert page.locator("text=Recruitment Performance Overview").is_visible()
    assert page.locator("text=Job Sources").is_visible()
    assert page.locator("text=Hiring Funnel").is_visible()

    # ===== Metric cards =====
    assert page.locator("text=Total Candidates").is_visible()
    assert page.locator("text=Active Jobs").is_visible()
    assert page.locator("text=Interviews Completed").is_visible()
    assert page.locator("text=Hiring Rate").is_visible()

    # ===== Footer timestamp =====
    assert page.locator("text=Last updated").is_visible()