from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from scraping.webscraper import doScraping
import multiprocessing
import os
import json
import boto3
from botocore.exceptions import ClientError

#example to commit variables us-east-1
email_post_args = reqparse.RequestParser()
email_post_args.add_argument("email",type=str,help="the receptor", required=True)
email_post_args.add_argument("subject",type=str,help="the message subject", required=True)
email_post_args.add_argument("body_html",type=str,help="the message content", required=True)

SENDER  = 'torres.hernandez.jefferson@gmail.com'
AWS_REGION = "us-east-1"
CHARSET = "UTF-8"

client = boto3.client(
    'ses',
    aws_access_key_id='AKIAJLSX5YKNJGVW5KWA',
    aws_secret_access_key='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',
    region_name=AWS_REGION
)



def sedMessage(params):
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    params["email"],
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': params["body_html"],
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': '',
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': params["subject"],
                },
            },
            Source=SENDER
        )
        # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

class email(Resource):
    def post(self):
        args = email_post_args.parse_args()
        sedMessage(args)
        return 'success',201