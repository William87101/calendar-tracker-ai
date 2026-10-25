# calendar_tracker.py - Version 2
# Added recurring events support
# Generated with AI assistance (Claude)

events = []

def add_event(date, title, recurring=None):
    event = {"date": date, "title": title, "recurring": recurring}
    events.append(event)
    recur_str = f" (repeats {recurring})" if recurring else ""
    print(f"Event added: {title} on {date}{recur_str}")

def delete_event(title):
    for event in events:
        if event["title"] == title:
            events.remove(event)
            print(f"Deleted: {title}")
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
    print("Calendar Tracker v2 - Recurring Events")
    print("---------------------------------------")
    while True:
        print("\n1. Add event")
        print("2. Add recurring event")
        print("3. Delete event")
        print("4. List events")
        print("5. Quit")
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
                print("Invalid recurrence, defaulting to weekly")
                recur = "weekly"
            add_event(date, title, recurring=recur)
        elif choice == "3":
            title = input("Event title to delete: ").strip()
            delete_event(title)
        elif choice == "4":
            list_events()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

main()
