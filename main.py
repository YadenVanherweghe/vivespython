import csv
from database import (
    initialiseer_database,
    voeg_speler_toe,
    haal_alle_spelers_op,
    verwijder_speler
)


def lees_verplicht_tekst(prompt):
    while True:
        tekst = input(prompt).strip()
        if tekst:
            return tekst
        print("Gelieve een geldige tekst in te geven.")


def lees_getal(prompt):
    while True:
        invoer = input(prompt)
        try:
            return int(invoer)
        except ValueError:
            print("Gelieve een geldig getal in te geven.")


def lees_marktwaarde():
    while True:
        invoer = input("Marktwaarde (€) (bv. 500000 of 500.000): ")
        invoer = invoer.replace("€", "").replace(".", "").strip()

        try:
            return int(invoer)
        except ValueError:
            print("Gelieve een geldige marktwaarde in te geven.")


def toon_spelers():
    try:
        spelers = haal_alle_spelers_op()
    except Exception as fout:
        print("Fout bij het lezen van de database.")
        print(f"Details: {fout}")
        return

    if not spelers:
        print("Geen spelers gevonden.")
    else:
        print("\n--- SPELERS ZULTE WAREGEM ---")
        for speler in spelers:
            print(speler)


def voeg_speler_toe_menu():
    print("\n--- NIEUWE SPELER TOEVOEGEN ---")
    naam = lees_verplicht_tekst("Naam speler: ")
    leeftijd = lees_getal("Leeftijd: ")
    positie = lees_verplicht_tekst("Positie: ")
    rugnummer = lees_getal("Rugnummer: ")
    marktwaarde = lees_marktwaarde()
    nationaliteit = lees_verplicht_tekst("Nationaliteit: ")

    voeg_speler_toe(
        naam, leeftijd, positie,
        rugnummer, marktwaarde, nationaliteit
    )

    print("Speler succesvol toegevoegd!")


def verwijder_speler_menu():
    speler_id = lees_getal("Geef het ID van de speler die je wil verwijderen: ")
    verwijder_speler(speler_id)
    print("Speler verwijderd (indien ID bestond).")


def exporteer_spelers_naar_csv():
    spelers = haal_alle_spelers_op()

    if not spelers:
        print("Geen spelers om te exporteren.")
        return

    with open("spelers_zulte_waregem.csv", "w", newline="", encoding="utf-8") as bestand:
        schrijver = csv.writer(bestand)
        schrijver.writerow([
            "ID", "Naam", "Leeftijd", "Positie",
            "Rugnummer", "Marktwaarde", "Nationaliteit"
        ])

        for speler in spelers:
            schrijver.writerow([
                speler.id,
                speler.naam,
                speler.leeftijd,
                speler.positie,
                speler.rugnummer,
                speler.marktwaarde,
                speler.nationaliteit
            ])

    print("CSV-export gemaakt: spelers_zulte_waregem.csv")


def menu():
    initialiseer_database()

    while True:
        print("\n--- ZULTE WAREGEM SPELERS MENU ---")
        print("1. Toon spelers")
        print("2. Voeg speler toe")
        print("3. Verwijder speler")
        print("4. Exporteer spelers naar CSV")
        print("5. Stop")

        keuze = input("Keuze: ")

        if keuze == "1":
            toon_spelers()
        elif keuze == "2":
            voeg_speler_toe_menu()
        elif keuze == "3":
            verwijder_speler_menu()
        elif keuze == "4":
            exporteer_spelers_naar_csv()
        elif keuze == "5":
            print("Programma stopt.")
            break
        else:
            print("Gelieve een geldige keuze in te geven (1-5).")


menu()
