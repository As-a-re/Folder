import winsound
import datetime

def set_schedule():
    """Collect user schedules and times for activities."""
    schedule = {}
    while True:
        activity = input("Enter the name of the activity (or 'done' to finish): ").strip()
        if activity.lower() == 'done':
            break
        time_str = input("Enter the time for {}: (format HH:MM) ".format(activity)).strip()
        try:
            time_obj = datetime.datetime.strptime(time_str, "%H:%M")
            schedule[activity] = time_obj.time()
        except ValueError:
            print("Invalid time format. Please use HH:MM format.")
    return schedule

def check_schedule(schedule):
    """Check the schedule and trigger alarm if time for activity is reached."""
    while True:
        current_time = datetime.datetime.now().time()
        for activity, time in schedule.items():
            if current_time.hour == time.hour and current_time.minute == time.minute:
                print("It's time for {}!".format(activity))
                trigger_alarm()


def trigger_alarm():
    """Trigger alarm sound."""
    duration_seconds = 10
    frequency = 440
    winsound.Beep(frequency, duration_seconds * 1000)

if __name__ == "__main__":
    print("Welcome to the Schedule Alarm!")
    user_schedule = set_schedule()
    print("Schedule set successfully!")
    check_schedule(user_schedule)
