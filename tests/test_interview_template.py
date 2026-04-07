import pytest
import time
from pages.interview_template_page import InterviewTemplatePage


@pytest.mark.smoke
def test_interview_template(dashboard_page):
    dashboard = dashboard_page
    page = dashboard.page
    template_page = InterviewTemplatePage(page)

    template_page.open()

    template_name = f"QA_Template_{int(time.time())}"
    template_page.enter_template_name(template_name)

    template_page.select_interview_round("Technical")
    template_page.select_language("English")

    template_page.add_questions(15)

    # Critical AI fill step
    template_page.ai_generate_questions("15 Questions")

    template_page.save_template()
    template_page.assert_template_created()