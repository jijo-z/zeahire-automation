import os
import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.dashboard_page import DashboardPage


# ================= CONFIG ================= #

BASE_URL = os.getenv("BASE_URL", "https://qa.zeahire.ai")
EMAIL = os.getenv("EMAIL", "Jijo@zealogics.com")
PASSWORD = os.getenv("PASSWORD", "Admin@123")

HEADLESS = os.getenv("HEADLESS", "true" if os.getenv("CI") else "false").lower() == "true"
SLOW_MO = int(os.getenv("SLOW_MO", "0"))


# ================= CLI OPTION ================= #

def pytest_addoption(parser):
    parser.addoption(
        "--pw-trace",
        action="store_true",
        default=False,
        help="Enable Playwright tracing"
    )


# ================= PLAYWRIGHT ================= #

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(
        headless=HEADLESS,
        slow_mo=SLOW_MO
    )
    yield browser
    browser.close()


# ================= CONTEXT ================= #

@pytest.fixture(scope="function")
def context(browser, request):

    context = browser.new_context(
        viewport={"width": 1440, "height": 900},
        ignore_https_errors=True
    )

    trace_enabled = request.config.getoption("--pw-trace")

    if trace_enabled:
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

    yield context

    if trace_enabled:
        trace_dir = "reports/traces"
        os.makedirs(trace_dir, exist_ok=True)

        test_name = request.node.name.replace("/", "_")
        trace_path = os.path.join(trace_dir, f"{test_name}.zip")

        context.tracing.stop(path=trace_path)

        # Attach trace only if test failed
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            if os.path.exists(trace_path):
                allure.attach.file(
                    trace_path,
                    name="Playwright Trace",
                    attachment_type=allure.attachment_type.ZIP
                )

    context.close()


# ================= PAGE ================= #

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


# ================= AUTH ================= #

@pytest.fixture(scope="function")
def dashboard_page(page):

    page.goto(f"{BASE_URL}/login", wait_until="domcontentloaded")

    page.fill("input[name='email']", EMAIL)
    page.fill("input[name='password']", PASSWORD)
    page.click("button[type='submit']")

    page.wait_for_url("**/dashboard", timeout=30000)
    page.wait_for_load_state("networkidle")

    assert page.url.endswith("/dashboard")

    return DashboardPage(page)


# ================= FAILURE HOOK ================= #

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

    # Attach screenshot on failure
    if rep.when == "call" and rep.failed:

        page = item.funcargs.get("page", None)

        if page:
            try:
                png_bytes = page.screenshot(full_page=True)

                allure.attach(
                    png_bytes,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as e:
                print(f"Screenshot capture failed: {e}")