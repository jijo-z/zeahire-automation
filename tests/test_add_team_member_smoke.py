import pytest
import time
from pages.team_management_page import TeamManagementPage


@pytest.mark.smoke
def test_add_team_member_smoke(dashboard_page):
    """
    Smoke test:
    - Open Team Management
    - Add a team member
    - Verify invitation success
    """

    dashboard = dashboard_page
    page = dashboard.page
    team_page = TeamManagementPage(page)

    # ================= OPEN PAGE =================
    team_page.open()

    # ================= ADD MEMBER =================
    team_page.open_add_member_dialog()

    unique_email = f"qa.user.{int(time.time())}@example.com"

    team_page.fill_basic_info(
        email=unique_email,
        password="Admin@123",
        first="QA",
        last="User",
        phone="9999999999"
    )

    team_page.select_role("Recruiter")

    team_page.submit()

    # ================= VERIFY =================
    team_page.assert_member_added()