from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as et


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, data: str):
        if data.endswith(".xml"):
            with open(data) as XmlFile:
                return et.parse(XmlFile)
        raise ValueError("Arquivo inválido")
