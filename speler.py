class Speler:
    def __init__(self, speler_id, naam, leeftijd, positie, rugnummer, marktwaarde, nationaliteit):
        self.id = speler_id
        self.naam = naam
        self.leeftijd = leeftijd
        self.positie = positie
        self.rugnummer = rugnummer
        self.marktwaarde = marktwaarde
        self.nationaliteit = nationaliteit

    def __str__(self):
        return (
            f"{self.id} | {self.naam} | {self.leeftijd} jaar | "
            f"{self.positie} | Rugnr {self.rugnummer} | "
            f"€{self.marktwaarde:,} | {self.nationaliteit}"
        )
