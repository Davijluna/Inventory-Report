from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, data: str):
        if data.endswith(".xml"):
            with open(data) as XmlFile:
                return xmltodict.parse(XmlFile.read())['dataset']['record']
        raise ValueError("Arquivo inválido")
