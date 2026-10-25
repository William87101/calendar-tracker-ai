# calendar_tracker.py - Version 5
# Added CSV export
# Generated with AI assistance (Claude)

import json
import os
import datetime
import csv

SAVE_FILE = "events.json"
EXPORT_FILE = "events_export.csv"
events = []

def load_events():
    global events
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            events = json.load(f)
        print(f"Loaded {len(events)} events from {SAVE_FILE}")
    else:
        events = []

def save_events():
    with open(SAVE_FILE, "w") as f:
        json.dump(events, f, indent=2)

def export_csv():
    if not events:
        print("No events to export.")
        return
    with open(EXPORT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "title", "recurring"])
        writer.writeheader()
        for event in events:
            writer.writerow({
                "date": event.get("date", ""),
                "title": event.get("title", ""),
                "recurring": event.get("recurring") or ""
            })
    print(f"Exported {len(events)} events to {EXPORT_FILE}")

def check_reminders():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    reminders = []
    for event in events:
        try:
            event_date = datetime.date.fromisoformat(event["date"])
            if event_date == today:
                reminders.append(f"  TODAY: {event['title']}")
            elif event_date == tomorrow:
                reminders.append(f"  TOMORROW: {event['title']}")
        except ValueError:
            pass
    if reminders:
        print("\n*** REMINDERS ***")
        for r in reminders:
            print(r)
        print("*****************")

def add_event(date, title, recurring=None):
    event = {"date": date, "title": title, "recurring": recurring}
    events.append(event)
    recur_str = f" (repeats {recurring})" if recurring else ""
    print(f"Event added: {title} on {date}{recur_str}")
    save_events()

def delete_event(title):
    for event in events:
        if event["title"] == title:
            events.remove(event)
            print(f"Deleted: {title}")
            save_events()
            return
    print(f"Event not found: {title}")

def list_events():
    if not events:
        print("No events scheduled.")
        return
    print("\nUpcoming Events:")
    for event in events:
        recur = f" [{event['recurring']}]" if event.get("recurring") else ""
        print(f"  {event['date']} - {event['title']}{recur}")

def main():
    print("Calendar Tracker v5 - CSV Export")
    print("---------------------------------")
    load_events()
    check_reminders()
    while True:
        print("\n1. Add event")
        print("2. Add recurring event")
        print("3. Delete event")
        print("4. List events")
        print("5. Check reminders")
        print("6. Export to CSV")
        print("7. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            date = input("Date (YYYY-MM-DD): ").strip()
            title = input("Event title: ").strip()
            add_event(date, title)
        elif choice == "2":
            date = input("Start date (YYYY-MM-DD): ").strip()
            title = input("Event title: ").strip()
            print("Recurrence: daily / weekly / monthly")
            recur = input("Choose: ").strip()
            if recur not in ["daily", "weekly", "monthly"]:
                recur = "weekly"
            add_event(date, title, recurring=recur)
        elif choice == "3":
            title = input("Event title to delete: ").strip()
            delete_event(title)
        elif choice == "4":
            list_events()
        elif choice == "5":
            check_reminders()
        elif choice == "6":
            export_csv()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

main()
