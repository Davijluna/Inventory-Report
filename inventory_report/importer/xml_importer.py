from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET
# import xmltodict as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, data: str):
        if data.endswith(".xml"):
            # with open(data) as XmlFile:
            # return ET.parse(XmlFile.read())['dataset']['record']
            with open(data, mode='r') as test:
                root = ET.parse(test).getroot()
                return [
                    {line.tag: line.text for line in record}
                    for record in root
                ]
        raise ValueError("Arquivo inválido")
