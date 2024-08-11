import time
import threading
from plyer import notification
import winsound

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='TimerApp',
        timeout=10
    )

def play_alarm():
    duration = 1000  # milliseconds
    freq = 440  # Hz
    for _ in range(5):  # Play sound 5 times
        winsound.Beep(freq, duration)
        time.sleep(0.5)  # 0.5 seconds between beeps

def timer(minutes):
    seconds = minutes * 60
    print(f"Timer set for {minutes} minutes.")
    notify("Timer Started", f"Timer set for {minutes} minutes.")
    time.sleep(seconds)
    print("Time's up!")
    notify("Timer Finished", "Time's up!")
    play_alarm()

def start_timer():
    minutes = int(input("Enter the time in minutes: "))
    timer_thread = threading.Thread(target=timer, args=(minutes,))
    timer_thread.start()

if __name__ == "__main__":
    start_timer()
