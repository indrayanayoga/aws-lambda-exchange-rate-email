import requests
import json
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config

def handler(event, context):
    #Set the Currency Exchange API
    url = 'https://api.exchangeratesapi.io/v1/latest?access_key=XXXXXXXXXXXXXXXX&symbols=IDR'
 
    #Fetch the "IDR" part from the JSON response
    response = requests.get(url,verify=False).json()
    IDR = response['rates']['IDR']

    #If needed, you can use a dummy JSON response like below
    #response = '{"success": "True", "timestamp": "1746274744", "base": "EUR", "date": "2025-05-03", "rates": {"IDR": "18609.868588"}}'
    #response_json = json.loads(response)
    #IDR = response_json['rates']['IDR']

    #Use BOTO library to connect to Amazon SES
    client = boto3.client(
                "ses",
                aws_access_key_id="XXXXXXXXX",
                aws_secret_access_key="YYYYYYYYYY",
                region_name="us-east-1"
            )
    SENDER = "XXXXXXX@gmail.com"
    RECIPIENT = "XXXXXXXXX@yahoo.co.id"
    SUBJECT = "Today's EUR to IDR Rate"
    BODY_TEXT = ("Good morning, Indrayana!\r\n\n"
                 f"Today, 1 EUR equals {IDR} in IDR.\n\n"
                 "Have a great day!"
                )
    CHARSET = "UTF-8"

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        return(e.response['Error']['Message'])
    else:
        return("Email sent!")
