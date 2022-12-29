from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, data: str):
        if data.endswith(".json"):
            with open(data, mode='r') as jeisao:
                return json.load(jeisao)
        raise ValueError("Arquivo inválido")
