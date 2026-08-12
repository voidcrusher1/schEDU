# ========================================
#              SchEDU
#     Student Schedule Planner
# ========================================

schedules = []


def add_schedule():
    print("\n========================================")
    print("            ADD SCHEDULE")
    print("========================================")

    subject = input("Enter Subject: ")
    day = input("Enter Day: ")
    start_time = input("Enter Start Time: ")
    end_time = input("Enter End Time: ")
    room = input("Enter Room: ")

    schedule = {
        "subject": subject,
        "day": day,
        "start_time": start_time,
        "end_time": end_time,
        "room": room
    }

    schedules.append(schedule)

    print("\nSchedule added successfully!")
    input("Press Enter to continue...")


def view_schedule():
    print("\n========================================")
    print("           MY SCHEDULE")
    print("========================================")

    if len(schedules) == 0:
        print("No schedules available.")
    else:
        print(f"{'Subject':<22} {'Day':<12} {'Time':<18} {'Room'}")
        print("-" * 70)

        for schedule in schedules:
            time = schedule["start_time"] + " - " + schedule["end_time"]

            print(
                f"{schedule['subject']:<22} "
                f"{schedule['day']:<12} "
                f"{time:<18} "
                f"{schedule['room']}"
            )

    print("========================================")
    input("Press Enter to return to Main Menu...")


def edit_schedule():
    print("\n========================================")
    print("           EDIT SCHEDULE")
    print("========================================")

    if len(schedules) == 0:
        print("No schedules available.")
        input("Press Enter to continue...")
        return

    for i, schedule in enumerate(schedules, start=1):
        print(f"[{i}] {schedule['subject']} - {schedule['day']}")

    try:
        choice = int(input("\nEnter schedule number to edit: "))

        if choice < 1 or choice > len(schedules):
            print("\nERROR: Invalid schedule number!")
            input("Press Enter to continue...")
            return

        schedule = schedules[choice - 1]

        print("\nEnter new information:")

        schedule["subject"] = input("Enter Subject: ")
        schedule["day"] = input("Enter Day: ")
        schedule["start_time"] = input("Enter Start Time: ")
        schedule["end_time"] = input("Enter End Time: ")
        schedule["room"] = input("Enter Room: ")

        print("\nSchedule updated successfully!")

    except ValueError:
        print("\nERROR: Please enter a valid number.")

    input("Press Enter to continue...")


def delete_schedule():
    print("\n========================================")
    print("          DELETE SCHEDULE")
    print("========================================")

    if len(schedules) == 0:
        print("No schedules available.")
        input("Press Enter to continue...")
        return

    for i, schedule in enumerate(schedules, start=1):
        print(f"[{i}] {schedule['subject']} - {schedule['day']}")

    try:
        choice = int(input("\nEnter schedule number to delete: "))

        if choice < 1 or choice > len(schedules):
            print("\nERROR: Invalid schedule number!")
            input("Press Enter to continue...")
            return

        deleted = schedules.pop(choice - 1)

        print(f"\n{deleted['subject']} schedule deleted successfully!")

    except ValueError:
        print("\nERROR: Please enter a valid number.")

    input("Press Enter to continue...")


def main():
    while True:
        print("\n========================================")
        print("              SchEDU")
        print("     Student Schedule Planner")
        print("========================================")
        print("[1] Add Schedule")
        print("[2] View Schedule")
        print("[3] Edit Schedule")
        print("[4] Delete Schedule")
        print("[5] Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_schedule()

        elif choice == "2":
            view_schedule()

        elif choice == "3":
            edit_schedule()

        elif choice == "4":
            delete_schedule()

        elif choice == "5":
            print("\nThank you for using SchEDU!")
            break

        else:
            print("\n========================================")
            print("               ERROR")
            print("========================================")
            print("Invalid choice!")
            print("Please enter a number from 1 to 5.")
            input("Press Enter to try again...")


# Start the program
main()