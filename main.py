import os
from reminder import Reminder
from datetime import datetime

from sms_email import send_sms_via_email
from dotenv import load_dotenv

load_dotenv()

CONTACTS=[
    os.getenv('CONTACT_NUMBER_1'),
    os.getenv('CONTACT_NUMBER_2')
    ]

today = datetime.now()
tasks_for_today = []

reminders = [
                Reminder('Water all plants', 2, datetime(2022, 5, 21)),
                Reminder('Take out Black bin', 2, datetime(2022, 5, 16)),
                Reminder('Take out Green bin', 2, datetime(2022, 5, 17)),
                Reminder('Take out Blue bin', 1, datetime(2022, 5, 17)),
                Reminder('Check Water Softener level', 5, datetime(2022, 5, 14)),
                Reminder('Check HEPA Filter', 15, datetime(2022, 5, 14)),
                Reminder('Check Furnace Filter', 25, datetime(2022, 5, 14))
            ]

for task in reminders:
    weeks_since_start = (today - task.first_started).days / 7 # converting days to weeks
    if weeks_since_start % task.frequency == 0.0:
        tasks_for_today.append(task.name)

tasks = '\n\n'.join(tasks_for_today)
message = f"Tasks for Today\n\n{tasks}"
print(message)
if tasks_for_today:
    for contact in CONTACTS:
        print('Sending message to: ', contact)
        send_sms_via_email(contact, message, 'Telus')