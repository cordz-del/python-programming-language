# test_email_sender.py
import unittest
from unittest.mock import patch
from email_sender import send_email

class TestEmailSender(unittest.TestCase):
    @patch("smtplib.SMTP")
    def test_send_email(self, mock_smtp):
        instance = mock_smtp.return_value.__enter__.return_value
        send_email("smtp.example.com", 587, "user@example.com", "password",
                   "from@example.com", "to@example.com", "Test Subject", "Test Body")
        instance.starttls.assert_called_once()
        instance.login.assert_called_once_with("user@example.com", "password")
        instance.sendmail.assert_called_once()
        print("test_send_email passed.")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
