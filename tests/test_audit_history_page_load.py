import pytest
from conftest import page
from pages.audit_history_page import AuditHistoryPage


@pytest.mark.smoke
def test_audit_history_page_load(dashboard_page):

    dashboard = dashboard_page
    page = dashboard.page

    # ===== Navigate using sidebar (better than direct URL) =====
    page.get_by_role("link", name="Audit History").click()

    # ===== Wait for page URL =====
    page.wait_for_url("**/organization-audit-history")

    audit_page = AuditHistoryPage(page)

    # ===== Page Load Validation =====
    page.get_by_role("heading", name="Organization Audit History").first.wait_for()
    page.get_by_role("heading", name="Organization Audit History").first.wait_for()

    # ===== Components Validation =====
    audit_page.refresh_button.wait_for()
    audit_page.export_button.wait_for()
    audit_page.search_input.wait_for()

    assert audit_page.refresh_button.is_visible()
    assert audit_page.export_button.is_visible()
    assert audit_page.search_input.is_visible()


    page.get_by_role("heading", name="Organization Audit History").first.wait_for()