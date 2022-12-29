from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, data: str):
        if data.endswith(".csv"):
            with open(data) as CsvFile:
                return csv.reader(CsvFile)
        raise ValueError("Arquivo inválido")
