import smtplib
import os
from email.mime.text import MIMEText

def send_email():
    sender = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receivers = os.getenv("EMAIL_RECEIVERS").split(",")

    subject = "ZeaHire Automation Report"

    report_url = "https://jijo-z.github.io/zeahire-automation/"

    body = f"""
Automation Execution Completed

View Full Allure Report:
{report_url}

Regards,
Automation Bot
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(receivers)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receivers, msg.as_string())
    
if __name__ == "__main__":
    send_email()        