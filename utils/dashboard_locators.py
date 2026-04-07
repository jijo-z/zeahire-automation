class DashboardLocators:
    HIRING_STATISTICS_TITLE = "h1:has-text('Hiring Statistics')"
    NEW_JOB_BUTTON = "a[href='/jobs/create']"
    NOTIFICATIONS_BUTTON = "button:has(img[alt='Notifications'])"
    PROFILE_SECTION = "button[aria-haspopup='menu']"

    CANDIDATES_CARD = "a[href='/candidates']"
    ACTIVE_JOBS_CARD = "text=Active Jobs"
    INTERVIEWS_COMPLETED_CARD = "text=Interviews Completed"
    HIRING_RATE_CARD = "text=Hiring Rate"
    REJECTED_CANDIDATES_CARD = "text=Rejected Candidates"

    APPLICATIONS_CHART = "text=Applications"
    DEPARTMENT_CHART = "text=Application by Department"

    RECENT_APPLICATIONS_TAB = "button:has-text('Recent Applications')"
    RECENT_JOBS_TAB = "button:has-text('Recent Jobs')"

    TABLE = "table"
    INTERVIEW_CALENDAR = "text=Interview Calendar"
    HIRING_PIPELINE = "text=Hiring Pipeline"