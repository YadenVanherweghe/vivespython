import csv
from database import init_db, add_task, get_all_tasks, delete_task


def show_tasks():
    tasks = get_all_tasks()

    if not tasks:
        print("Geen taken gevonden.")
    else:
        print("\nTaken:")
        for task in tasks:
            print(task)


def add_task_menu():
    title = input("Geef een taak: ")
    add_task(title)
    print("Taak toegevoegd!")


def delete_task_menu():
    task_id = input("Geef het ID van de taak die je wil verwijderen: ")
    delete_task(task_id)
    print("Taak verwijderd (als het ID bestond).")


def export_tasks_to_csv():
    tasks = get_all_tasks()

    if not tasks:
        print("Geen taken om te exporteren.")
        return

    with open("taken_export.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Taak"])

        for task in tasks:
            writer.writerow([task.id, task.title])

    print("Taken geëxporteerd naar taken_export.csv")


def menu():
    init_db()

    while True:
        print("\n--- TAKEN MENU ---")
        print("1. Toon taken")
        print("2. Voeg taak toe")
        print("3. Verwijder taak")
        print("4. Exporteer taken naar CSV")
        print("5. Stop")

        choice = input("Keuze: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task_menu()
        elif choice == "3":
            delete_task_menu()
        elif choice == "4":
            export_tasks_to_csv()
        elif choice == "5":
            print("Programma stopt.")
            break
        else:
            print("Ongeldige keuze")


menu()
