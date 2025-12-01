import schedule
import time
from plyer import notification


def show_notification(message):
    notification.notify(
        title="Reminder",
        message=message,
        timeout=10
    )


def add_reminder(text, reminder_time):
    schedule.every().day.at(reminder_time).do(show_notification, message=text)
    print(f"Reminder added for {reminder_time}: {text}")


if __name__ == "__main__":
    while True:
        text = input("Enter your reminder text: ")
        reminder_time = input("Enter time (HH:MM format): ")
        add_reminder(text, reminder_time)
        print("Waiting for reminder...")

        while True:
            schedule.run_pending()
            time.sleep(1)

