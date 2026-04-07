import time
import pytest
from pages.create_job_page import CreateJobPage


@pytest.mark.smoke
def test_create_job_smoke(dashboard_page):
    dashboard = dashboard_page
    page = dashboard.page
    create_job = CreateJobPage(page)

    job_title = f"QA Engineer {int(time.time())}"

    create_job.open()
    create_job.fill_basic_details(job_title)
    create_job.fill_information_page()
    create_job.fill_location_page()
    create_job.create_job()
    create_job.assert_job_created()