import json
import os
import random
from datetime import date, datetime


FILE_NAME = "capsules.json"


class Capsule:
    def __init__(self, title, message, unlock_date, mood, capsule_id):
        self.id = capsule_id
        self.title = title
        self.message = message
        self.unlock_date = unlock_date
        self.mood = mood

    def features(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
            "unlock_date": self.unlock_date,
            "mood": self.mood
        }

    def __str__(self):
        text = (
            f"ID: {self.id} | "
            f"{self.title} | "
            f"Unlock: {self.unlock_date}"
        )

        if self.mood:
            text += f" | Mood: {self.mood}"

        return text


def generate_id(capsules):
    existing_ids = []

    for capsule in capsules:
        existing_ids.append(capsule.id)

    while True:
        new_id = random.randint(1000, 9999)

        if new_id not in existing_ids:
            return new_id


def save_capsules(capsules):
    data = []

    for capsule in capsules:
        data.append(capsule.features())

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_capsules():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)
        return []

    with open(FILE_NAME, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return []

    capsules = []

    for item in data:
        capsule = Capsule(
            item["title"],
            item["message"],
            item["unlock_date"],
            item["mood"],
            item["id"]
        )
        capsules.append(capsule)

    return capsules


def display_menu():
    print("\nDIGITAL TIME CAPSULE")
    print("1. Create capsule")
    print("2. View capsules")
    print("3. Open unlocked capsules")
    print("4. Search capsules")
    print("5. Delete capsule")
    print("6. Exit")


def create_capsule(capsules):
    print("\nCreate New Capsule")

    while True:
        title = input("Title: ").strip()
        if title:
            break
        print("Title cannot be empty.")

    while True:
        message = input("Message: ").strip()
        if message:
            break
        print("Message cannot be empty.")

    while True:
        unlock_date = input("Unlock date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(unlock_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format.")

    mood = input("Current mood (optional): ").strip()

    capsule_id = generate_id(capsules)

    capsule = Capsule(
        title,
        message,
        unlock_date,
        mood,
        capsule_id
    )

    capsules.append(capsule)
    save_capsules(capsules)

    print(f"Capsule created with ID {capsule.id}")


def view_capsules(capsules):
    if not capsules:
        print("No capsules found.")
        return

    print("\nYour Capsules:")

    for capsule in capsules:
        print(capsule)


def open_capsules(capsules):
    today = str(date.today())

    found = False

    for capsule in capsules:
        if capsule.unlock_date <= today:
            found = True

            print("\nMEMORY UNLOCKED")
            print(f"Title: {capsule.title}")
            print(f"Mood: {capsule.mood}")
            print(capsule.message)

    if not found:
        print("No capsules are ready yet.")


def search_capsules(capsules):
    keyword = input(
        "Search keyword: "
    ).lower()

    found = False

    for capsule in capsules:
        if keyword in capsule.title.lower():
            print(capsule)
            found = True

    if not found:
        print("No matching capsules.")


def delete_capsule(capsules):
    view_capsules(capsules)

    try:
        target = int(
            input("Enter capsule ID to delete: ")
        )

    except ValueError:
        print("Invalid ID.")
        return

    for capsule in capsules:
        if capsule.id == target:
            capsules.remove(capsule)
            save_capsules(capsules)
            print("Capsule deleted.")
            return

    print("Capsule not found.")


def main():
    capsules = load_capsules()

    while True:

        display_menu()

        choice = input(
            "Choose: "
        )

        if choice == "1":
            create_capsule(capsules)

        elif choice == "2":
            view_capsules(capsules)

        elif choice == "3":
            open_capsules(capsules)

        elif choice == "4":
            search_capsules(capsules)

        elif choice == "5":
            delete_capsule(capsules)

        elif choice == "6":
            save_capsules(capsules)
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
