import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Get values from GitHub secrets (mapped in YAML)
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")

if not EMAIL_USER or not EMAIL_PASS or not TO_EMAIL:
    raise ValueError("❌ Missing email environment variables")

# Email content
msg = MIMEMultipart()
msg["From"] = EMAIL_USER
msg["To"] = TO_EMAIL
msg["Subject"] = "ZeaHire Automation Report"

body = f"""
Hi Team,

✅ Automation run completed.

📊 View Report:
https://jijo-z.github.io/zeahire-automation/

Regards,
Automation Bot
"""

msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.send_message(msg)
    server.quit()

    print("✅ Email sent successfully")

except Exception as e:
    print("❌ Error sending email:", str(e))
    raise