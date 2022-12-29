'''
author: Rohit Sharma
Date: 29-Jul-2022

***SMS Sender using Telnyx API***
'''
import requests

# Set the API endpoint URL and your API key
api_endpoint = "https://api.telnyx.com/v2/messages"
api_key = "###################"

# Set the phone number you want to send the SMS to, and the message you want to send
to_number = "+15551234567"
message = "This is a test SMS message"

# Set the headers for the HTTP request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Set the payload for the HTTP request
payload = {
    "to": to_number,
    "text": message
}

# Send the SMS
response = requests.post(api_endpoint, json=payload, headers=headers)

# Check the response to see if the SMS was sent successfully
if response.status_code == 201:
    print("SMS sent successfully")
else:
    print(f"Error sending SMS: {response.status_code}")
