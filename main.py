import csv
class SupportArende:
    def __init__(self, id, kund, kategori, prioritet, status):
        self.id = id
        self.kund = kund
        self.kategori = kategori
        self.prioritet = prioritet
        self.status = status

    def visa_info(self):
        return f"Ärende {self.id}: {self.kund} - {self.kategori} - {self.prioritet} - {self.status}"



arenden = []

with open("supportarenden.csv", encoding="utf-8") as fil:
    text = csv.DictReader(fil)

    for rad in text:
        arende = SupportArende(
            rad["id"],
            rad["kund"],
            rad["kategori"],
            rad["prioritet"],
            rad["status"]
        )

        arenden.append(arende)

for arende in arenden:
    print(arende.visa_info())
        