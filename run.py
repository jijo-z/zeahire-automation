import os
import subprocess
import smtplib
from email.mime.text import MIMEText

# Run tests
result = subprocess.run(["pytest", "-v"], capture_output=True, text=True)

# Email content
subject = "Automation Test Result"
body = f"""
Test Execution Completed

STATUS: {"PASS" if result.returncode == 0 else "FAIL"}

OUTPUT:
{result.stdout}
"""

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = os.getenv("EMAIL_USER")

# 👉 Add BOTH emails here
recipients = [
    os.getenv("EMAIL_USER"),
    "secondperson@gmail.com"
]

msg["To"] = ", ".join(recipients)

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
    server.sendmail(
        os.getenv("EMAIL_USER"),
        recipients,
        msg.as_string()
    )