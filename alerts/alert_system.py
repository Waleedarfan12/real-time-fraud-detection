import smtplib
from email.mime.text import MIMEText

def send_email_alert(tx):
    sender = "your_email@gmail.com"
    receiver = "your_email@gmail.com"
    password = "your_app_password"

    subject = "🚨 Fraud Transaction Alert"
    body = f"""
    Fraud detected!

    User ID: {tx['user_id']}
    Amount: {tx['amount']}
    Type: {tx['transaction_type']}
    Location: {tx['location']}
    Device: {tx['device']}
    Time: {tx['timestamp']}
    """

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("📧 Email alert sent!")
    except Exception as e:
        print("❌ Email failed:", e)