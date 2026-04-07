# save_login.py

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://qa.zeahire.ai/login")

    print("Login manually in the browser...")
    input("Press ENTER after login is complete")

    context.storage_state(path="login.json")
    print("Login state saved!")