# Importerar csv-modulen så att vi kan läsa CSV-filer.
import csv


# Skapar en klass som fungerar som en mall för supportärenden.
class SupportArende:

    # __init__ körs automatiskt när ett nytt objekt skapas.
    # self syftar på det objekt som skapas.
    def __init__(self, id, kund, kategori, prioritet, status):

        # Sparar informationen som attribut i objektet.
        self.id = id
        self.kund = kund
        self.kategori = kategori
        self.prioritet = prioritet
        self.status = status

    # En metod som skapar en läsbar text om supportärendet.
    def visa_info(self):

        # return skickar tillbaka texten utan att skriva ut den.
        return f"Ärende {self.id}: {self.kund} - {self.kategori} - {self.prioritet} - {self.status}"


# Skapar en tom lista där alla supportärenden ska sparas.
arenden = []


# Öppnar CSV-filen. with ser till att filen stängs automatiskt.
# utf-8 gör att svenska bokstäver kan läsas korrekt.
with open("supportarenden.csv", encoding="utf-8") as fil:

    # Läser CSV-filen och gör varje rad till en dictionary.
    # Kolumnrubrikerna används som nycklar.
    text = csv.DictReader(fil)

    # Går igenom CSV-filen, en rad i taget.
    for rad in text:

        # Skapar ett nytt objekt av klassen SupportArende.
        # Värdena hämtas från den aktuella CSV-raden.
        arende = SupportArende(
            rad["id"],
            rad["kund"],
            rad["kategori"],
            rad["prioritet"],
            rad["status"]
        )

        # Lägger till det nya objektet i listan arenden.
        arenden.append(arende)


# Går igenom alla sparade objekt i listan.
for arende in arenden:

    # Anropar objektets metod och skriver ut informationen.
    print(arende.visa_info())