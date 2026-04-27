import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Get values from GitHub Secrets
EMAIL_USER = os.environ.get("EMAIL_USER")        # your gmail (sender)
EMAIL_PASS = os.environ.get("EMAIL_PASSWORD")    # gmail app password
TO_EMAIL = os.environ.get("TO_EMAIL")            # company email (receiver)

# Create message
msg = MIMEMultipart()
msg["From"] = EMAIL_USER
msg["To"] = TO_EMAIL
msg["Subject"] = "ZeaHire Automation Report"

# Email body (you can customize this)
body = """
Hi Team,

✅ Automation run completed successfully.

📊 View Report:
https://jijo-z.github.io/zeahire-automation/

Regards,  
Automation Bot
"""

msg.attach(MIMEText(body, "plain"))

try:
    # Connect to Gmail SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)

    # Send email
    server.send_message(msg)
    server.quit()

    print("✅ Email sent successfully")

except Exception as e:
    print("❌ Error sending email:", str(e))