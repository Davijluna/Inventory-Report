from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, data: str):
        if data.endswith(".csv", encoding="utf-8"):
            with open(data) as CsvFile:
                return csv.reader(CsvFile, delimiter=",", quotechar='"')
        raise ValueError("Arquivo inválido")
