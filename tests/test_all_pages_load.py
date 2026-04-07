# import pytest
# from pages.dashboard_page import DashboardPage
# from pages.jobs_page import JobsPage
# from pages.candidates_page import CandidatesPage
# from pages.interview_page import InterviewPage
# from pages.audit_history_page import AuditHistoryPage


# @pytest.mark.smoke
# def test_all_pages_load(dashboard_page):

#     page = dashboard_page

#     # ===== Dashboard =====
#     dashboard = DashboardPage(page)
#     dashboard.title.wait_for()
#     assert dashboard.title.is_visible()

#     # ===== Jobs =====
#     page.get_by_role("link", name="Jobs").click()
#     page.wait_for_url("**/jobs")

#     jobs = JobsPage(page)
#     jobs.title.wait_for()
#     assert jobs.title.is_visible()

#     # ===== Candidates =====
#     page.get_by_role("link", name="Candidates").click()
#     page.wait_for_url("**/candidates")

#     candidates = CandidatesPage(page)
#     candidates.title.wait_for()
#     assert candidates.title.is_visible()

#     # ===== Interviews =====
#     page.get_by_role("link", name="Interviews").click()
#     page.wait_for_url("**/interviews")

#     interviews = InterviewPage(page)
#     interviews.title.wait_for()
#     assert interviews.title.is_visible()

#     # ===== Audit History =====
#     page.get_by_role("link", name="Audit History").click()
#     page.wait_for_url("**/organization-audit-history")

#     audit = AuditHistoryPage(page)
#     audit.title.wait_for()
#     assert audit.title.is_visible()
    
#     settings_page = dashboard.go_to_settings()
#     assert settings_page.is_loaded(), "Settings page failed to load"
    
#     how_page = dashboard.go_to_how_it_works()
#     assert how_page.is_loaded(), "How It Works page failed to load"