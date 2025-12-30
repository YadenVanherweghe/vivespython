\# Zulte Waregem Spelersbeheer

**Auteur:** Yaden Vanherweghe  
**Opleiding:** Cyber Security  
**School:** VIVES Hogeschool

Deze applicatie is een command line programma geschreven in Python

waarmee spelers van \*\*SV Zulte Waregem\*\* beheerd kunnen worden.

De gegevens worden opgeslagen in een \*\*SQLite-database\*\*.



Dit project werd ontwikkeld in het kader van het vak \*\*Programming in Python\*\*



---



\## Doel van de applicatie



Het doel van deze applicatie is het beheren van spelersgegevens via de terminal.

De gebruiker kan spelers toevoegen, bekijken, verwijderen en exporteren naar een CSV-bestand.

Er werd extra aandacht besteed aan foutafhandeling en gebruiksvriendelijkheid.



---



\## Functionaliteiten



\- Spelers toevoegen met volgende gegevens:

&nbsp; - Naam

&nbsp; - Leeftijd

&nbsp; - Positie

&nbsp; - Rugnummer

&nbsp; - Marktwaarde

&nbsp; - Nationaliteit

\- Spelers tonen via de terminal

\- Spelers verwijderen op basis van ID

\- CSV-export van alle spelers

\- Gebruiksvriendelijke foutmeldingen bij:

&nbsp; - Ongeldige invoer (bv. letters i.p.v. cijfers)

&nbsp; - Openstaand CSV-bestand (bv. in Excel)

\- Geen crashes bij foutieve invoer



---



\## Gebruikte technologieën



\- \*\*Python 3\*\*

\- \*\*SQLite\*\*

\- \*\*Git \& GitHub\*\*



Er worden geen externe Python-packages gebruikt.

Alle gebruikte modules (`sqlite3`, `csv`, `datetime`) maken deel uit van de standaard Python-installatie.



---



\## Installatie \& opstarten



1\. Clone de repository:



git clone https://github.com/YadenVanherweghe/vivespython



2\. Ga naar de projectmap:



cd "Phyton taak"



3\. (Optioneel maar aanbevolen) Maak een virtuele omgeving aan en activeer deze:



python -m venv venv

venv\\Scripts\\activate



4\. Installeer de vereiste packages:



pip install -r requirements.txt



5\. Start de applicatie:



python main.py

