# calendar_tracker.py - Version 1
# Basic calendar app - add and delete events
# Generated with AI assistance (Claude)

events = []

def add_event(date, title):
    event = {"date": date, "title": title}
    events.append(event)
    print(f"Event added: {title} on {date}")

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
        print(f"  {event['date']} - {event['title']}")

def main():
    print("Calendar Tracker v1")
    print("-------------------")
    while True:
        print("\n1. Add event")
        print("2. Delete event")
        print("3. List events")
        print("4. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            date = input("Date (YYYY-MM-DD): ").strip()
            title = input("Event title: ").strip()
            add_event(date, title)
        elif choice == "2":
            title = input("Event title to delete: ").strip()
            delete_event(title)
        elif choice == "3":
            list_events()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

main()
