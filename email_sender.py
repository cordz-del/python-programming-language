# email_sender.py
import smtplib
from email.mime.text import MIMEText

def send_email(smtp_server, port, username, password, from_addr, to_addr, subject, body):
    """
    Sends an email using SMTP.
    
    Args:
        smtp_server (str): SMTP server address.
        port (int): SMTP port.
        username (str): SMTP username.
        password (str): SMTP password.
        from_addr (str): Sender's email address.
        to_addr (str): Recipient's email address.
        subject (str): Email subject.
        body (str): Email body text.
    """
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
    print("Email sent successfully.")

if __name__ == "__main__":
    # For real usage, supply valid SMTP credentials.
    print("send_email function is ready to be used.")
