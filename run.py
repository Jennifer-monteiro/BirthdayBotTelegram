""" from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

#Handler the start command

def start(update,context):
    update.message.reply_text("Hello! I am your bithday reminder bot. ")

#ADD BIRTHDAY

birthdays = {
    "Lorena": "20-01",
    "Jennifer": "25-01",
    "Raissa": "27-01",
    "Victoria": "03-03",
    "Sue": "23-03",
    "Gabi": "31-03",
    "Chai": "01-04",
    "Kese": "18-12",
    "test": "11-05"
}

def send_reminders(context):
    today = datetime.date.today()
    #Format day-month
    today_formatted = today.strftime("%d-%m")

    #check if a birthdfay match

    for name, birthday in birthdays.items():
        if birthday == today_formatted:
            context.bot.send_message(chat_id='', text=f"🎉🎂 HOJE É ANIVERSÁRIO DA {name}! PARABÉNS!! 🎂🎉")


def main():
    updater = Updater('', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Start the Bot
    updater.start_polling()
    print("Bot started! Listening for commands...")
    # Schedule birthday reminders to be sent daily
    job_queue = updater.job_queue
    job_queue.run_daily(send_reminders, time=datetime.time(hour=9))  # Adjust the time as needed

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main() 
 """

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

# Handler for the start command
def start(update, context):
    update.message.reply_text("Hello! I am your birthday reminder bot.")

# ADD BIRTHDAY
birthdays = {
    "Lorena": "20-01",
    "Jennifer": "25-01",
    "Raissa": "27-01",
    "Victoria": "03-03",
    "Sue": "23-03",
    "Gabi": "31-03",
    "Chai": "01-04",
    "Kese": "18-12",
    "test": "11-05"  # Added test birthday for debugging
}

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

# Handler for the start command
def start(update, context):
    update.message.reply_text("Hello! I am your birthday reminder bot.")

# ADD BIRTHDAY
birthdays = {
    "Lorena": "20-01",
    "Jennifer": "25-01",
    "Raissa": "27-01",
    "Victoria": "03-03",
    "Sue": "23-03",
    "Gabi": "31-03",
    "Chai": "01-04",
    "Kese": "18-12",
    "test": "11-05"  # Added test birthday for debugging
}

# Function to send birthday reminders
def send_reminders(context: CallbackContext):
    today = datetime.date.today()
    # Format day-month
    today_formatted = today.strftime("%d-%m")

    print("Today's date:", today_formatted)  # Debugging line

    # Check if a birthday matches today
    for name, birthday in birthdays.items():
        if birthday == today_formatted:
            try:
                context.bot.send_message(chat_id='', text=f"🎉🎂 HOJE É ANIVERSÁRIO DA {name}! PARABÉNS!! 🎂🎉")
            except Exception as e:
                print(f"Error sending birthday message for {name}: {str(e)}")

# Function to print current time (for debugging)
def print_current_time(context: CallbackContext):
    now = datetime.datetime.now()
    print("Current time:", now.strftime("%H:%M:%S"))  # Debugging line

def main():
    updater = Updater('', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Define a command handler for the /start command
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()
    print("Bot started! Listening for commands...")

    # Schedule birthday reminders to be sent daily
    job_queue = updater.job_queue
    job_queue.run_daily(send_reminders, time=datetime.time(hour=9, minute=24))

    # Schedule a job to print current time for debugging
    job_queue.run_repeating(print_current_time, interval=60)  # Prints current time every 60 seconds

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
