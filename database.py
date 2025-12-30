import sqlite3
import speler
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

DATABASE_NAAM = config["database"]["pad"]


def maak_connectie():
    return sqlite3.connect(DATABASE_NAAM)


def initialiseer_database():
    conn = maak_connectie()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS spelers (
            id INTEGER PRIMARY KEY,
            naam TEXT,
            leeftijd INTEGER,
            positie TEXT,
            rugnummer INTEGER,
            marktwaarde INTEGER,
            nationaliteit TEXT
        )
    """)

    conn.commit()
    conn.close()


def voeg_speler_toe(naam, leeftijd, positie, rugnummer, marktwaarde, nationaliteit):
    conn = maak_connectie()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO spelers
        (naam, leeftijd, positie, rugnummer, marktwaarde, nationaliteit)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (naam, leeftijd, positie, rugnummer, marktwaarde, nationaliteit))

    conn.commit()
    conn.close()


def haal_alle_spelers_op():
    conn = maak_connectie()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, naam, leeftijd, positie, rugnummer, marktwaarde, nationaliteit
        FROM spelers
    """)

    rijen = cursor.fetchall()
    conn.close()

    spelers = []
    for rij in rijen:
        spelers.append(
            speler.Speler(
                rij[0], rij[1], rij[2],
                rij[3], rij[4], rij[5], rij[6]
            )
        )

    return spelers


def verwijder_speler(speler_id):
    conn = maak_connectie()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM spelers WHERE id = ?",
        (speler_id,)
    )

    conn.commit()
    conn.close()
