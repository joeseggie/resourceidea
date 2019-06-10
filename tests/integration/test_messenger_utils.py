"""
Testing sending email.
"""
from app.messenger.utils import send_email

def test_send_mail():
    # Arrange
    SUBJECT = "Amazon SES Test (SDK for Python)"

    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto).")
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Amazon SES Test (SDK for Python)</h1>
      <p>This email was sent with
        <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
        <a href='https://aws.amazon.com/sdk-for-python/'>
          AWS SDK for Python (Boto)</a>.</p>
    </body>
    </html>
            """
    recipients = ['joseph.serunjogi@andela.com','joeseggie@gmail.com',]


    # Act
    result = send_email(recipients, SUBJECT, BODY_TEXT, BODY_HTML)

    # Assert
    assert isinstance(result, dict)
