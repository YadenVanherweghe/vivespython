import sqlite3
import csv


def init_db():
    conn = sqlite3.connect("taken.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_task():
    title = input("Geef een taak: ")

    conn = sqlite3.connect("taken.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )
    conn.commit()
    conn.close()

    print("Taak toegevoegd!")


def show_tasks():
    conn = sqlite3.connect("taken.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print("Geen taken gevonden.")
    else:
        print("\nTaken:")
        for task in tasks:
            print(f"{task[0]} - {task[1]}")

    conn.close()


def delete_task():
    task_id = input("Geef het ID van de taak die je wil verwijderen: ")

    conn = sqlite3.connect("taken.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    conn.close()

    print("Taak verwijderd (als het ID bestond).")


def export_tasks_to_csv():
    conn = sqlite3.connect("taken.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("Geen taken om te exporteren.")
        return

    with open("taken_export.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Taak"])
        writer.writerows(tasks)

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
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            export_tasks_to_csv()
        elif choice == "5":
            print("Programma stopt.")
            break
        else:
            print("Ongeldige keuze")


menu()