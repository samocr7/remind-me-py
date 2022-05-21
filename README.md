Routine house tasks that I need reminders for...

Neat thing I learnt: You can send emails as SMS messages!
Instead of using a paid API like Twilio to send text messages, you can send an email to `phoneNumber@yourCellProviderDomain`
Here's a list of cell provider domains: https://email2sms.info/

If you want to clone this repo and test it out, you will need to do the following:
- Have a GMAIL account without 2FA, or an app password to bypass 2FA. (Check out this link to set up an app password: https://myaccount.google.com/apppasswords)
- Run `pip install python-dotenv`
- Run `cp .env.template .env` to create your .env file with the required environment variables, and assign them
    - There are two contact environment variables; if you want to change this amount, add/remove them in the .env file AND the CONTACTS array in main.py
- Change the reminders array in main.py with whatever reminders you need
    - example: To create a task that reminds you every week, starting on May 21, 2022: `Reminder('My Task', 1, datetime(2022, 5, 21))`
- Add the cell provider email domain for your recipient's phone number in providers.py
- Run `python main.py` to run the program
