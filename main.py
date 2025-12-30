import sqlite3

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
        for task in tasks:
            print(f"{task[0]} - {task[1]}")

    conn.close()

def menu():
    init_db()

    while True:
        print("\n--- TAKEN MENU ---")
        print("1. Toon taken")
        print("2. Voeg taak toe")
        print("3. Stop")

        choice = input("Keuze: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            print("Programma stopt.")
            break
        else:
            print("Ongeldige keuze")

menu()