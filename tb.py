import time
import datetime
import os
import threading

# Your schedule (24-hour format)
schedule = {
    "09:00": "🧠 Deep Work Session #1 Start",
    "12:00": "🚶 Take a short break",
    "12:30": "🍽️ Lunch Time",
    "13:30": "🧠 Deep Work Session #2 Start",
    "16:00": "☕ Break Time",
    "16:30": "📞 Meetings / Light Work",
    "18:00": "🧘 Wind-down Work",
    "18:30": "🏋️ Workout / Hobby Time",
    "20:00": "📚 Learning / Side Projects",
    "22:00": "🎮 Chill / Free Time",
    "23:30": "🌙 Wind Down & No Screens",
    "00:00": "💤 Time to Sleep"
}

def alert(message):
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # ASCII animation
    frames = [
        f"\n⏰ {message} ⏰",
        f"\n⏳ {message} ⏳",
        f"\n🔔 {message} 🔔"
    ]
    for _ in range(5):  # show animation 5 times
        for frame in frames:
            print(frame)
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')

    print(f"\n=== {message} ===\n")

    # Optional: Play a sound (Windows example)
    try:
        import winsound
        winsound.Beep(1000, 500)  # frequency, duration
    except ImportError:
        pass  # Sound feature only for Windows in this example

def schedule_checker():
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now in schedule:
            alert(schedule[now])
            time.sleep(60)  # wait a minute before checking again
        time.sleep(10)  # check every 10 seconds

# Run it in a separate thread
if __name__ == "__main__":
    print("🔄 Time table alarm started. Press Ctrl+C to stop.")
    threading.Thread(target=schedule_checker).start()
