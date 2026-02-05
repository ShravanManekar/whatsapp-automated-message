import time
import os
from datetime import datetime
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Load credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

if not account_sid or not auth_token:
    raise Exception("Twilio credentials not found. Set environment variables first.")

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=message_body,
            to=f"whatsapp:{recipient_number}"
        )
        print(f"✅ Message sent successfully! SID: {message.sid}")
    except Exception as e:
        print("❌ An error occurred:", e)

# User inputs
name = input("Enter the recipient name: ")
recipient_number = input("Enter the recipient WhatsApp number with country code (+91XXXXXXXXXX): ")
message_body = input(f"Enter the message you want to send to {name}: ")

date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM): ")

# Combine date and time
schedule_datetime = datetime.strptime(
    f"{date_str} {time_str}", "%Y-%m-%d %H:%M"
)

current_datetime = datetime.now()
delay_seconds = (schedule_datetime - current_datetime).total_seconds()

if delay_seconds <= 0:
    print("❌ Scheduled time must be in the future.")
else:
    print(f"⏳ Message scheduled for {schedule_datetime}")
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number, message_body)
