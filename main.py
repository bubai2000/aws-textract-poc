import boto3
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = boto3.client("textract", aws_access_key_id=os.getenv(
    "AWS_ACCESS_KEY_ID"), aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"), region_name=os.getenv("REGION_NAME"))

with open("document.pdf", "rb") as file:
    pdf = bytearray(file.read())

response = client.detect_document_text(
    Document={'Bytes': pdf}
)

with open("response.json", "w") as file:
    json.dump(response, file)
