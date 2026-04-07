from datetime import datetime, timedelta
import pytest
from pages.schedule_interview_page import ScheduleInterviewPage


@pytest.mark.smoke
def test_schedule_interview_smoke(dashboard_page):
    dashboard = dashboard_page
    page = dashboard.page
    schedule_page = ScheduleInterviewPage(page)

    # OPEN drawer
    schedule_page.open()

    # SELECT job & template
    schedule_page.select_job("Test engineer")
    schedule_page.select_template("Quality Analyst_Level_1")

    # ADD candidate (no confirmation check)
    schedule_page.add_candidate("Jijo Eappen")

    # SET future datetime
    future_datetime = (
        datetime.now() + timedelta(minutes=3)
    ).strftime("%Y-%m-%dT%H:%M")
    schedule_page.set_datetime(future_datetime)

    # ⚠️ SKIP configure_interview (defaults already correct)

    # SUBMIT
    schedule_page.submit()

    # VERIFY success toast
    schedule_page.verify_success()