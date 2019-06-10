"""
Messenger utils.
"""
import os

import boto3
from botocore.exceptions import ClientError


def send_email(
        recipients: list,
        subject: str,
        message_text: str = None,
        message_html: str = None) -> dict:
    """
    Send email.

    Args:
        recipients {list}: List of email recipients.

        subject {str}: Email subject.

        message {str}: Email body.
    """
    SENDER = os.environ.get('AWS_SES_SENDER')
    # CONFIGURATION_SET = 'ConfigSet'
    AWS_REGION = os.environ.get('AWS_REGION')
    AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')
    CHARSET = "UTF-8"

    client = boto3.client(
        'ses',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': recipients
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': message_html
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': message_text
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': subject
                },
            },
            Source=f'ResourceIdea <{SENDER}>',
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    except ClientError as error:
        raise ValueError(
            f'Error sending message: {error.response["Error"]["Message"]}')
    else:
        return {
            'MessageId': response['MessageId'],
            'Success': True
        }
