import pytest
from conftest import page
from pages.resume_parsing_page import ResumeParsingPage


@pytest.mark.smoke
def test_resume_parsing_smoke(dashboard_page):
    """
    Smoke test:
    - Open Candidates
    - Add candidate
    - Associate job
    - Upload multiple resumes
    - Upload & parse
    - Verify success toast
    """

    dashboard = dashboard_page
    page = dashboard.page

    resume_page = ResumeParsingPage(page)

    resume_page.open_candidates_page()
    resume_page.open_add_candidate()

    resume_page.associate_job("AI full stack developer")

    resume_page.upload_resumes([
        "resources/sample_resume.pdf",
        "resources/sample_resume.doc",
        "resources/sample_resume.docx",
        "resources/sample_resume.txt",
    ])

    resume_page.upload_and_parse()

    resume_page.assert_upload_success()
