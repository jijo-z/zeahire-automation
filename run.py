import os
import subprocess
import smtplib
from email.mime.text import MIMEText


def run_tests():
    subprocess.run([
        "pytest",
        "-m", "smoke",
        "--alluredir=reports/allure-results"
    ])


def send_email():
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receivers = os.getenv("EMAIL_RECEIVERS").split(",")

    report_url = "https://jijo-z.github.io/zeahire-automation/"

    body = f"""
Automation Execution Completed

View Report:
{report_url}
"""

    msg = MIMEText(body)
    msg["Subject"] = "Automation Report"
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receivers, msg.as_string())


# 🚀 MAIN FLOW
if __name__ == "__main__":
    run_tests()
    send_email()