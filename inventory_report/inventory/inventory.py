# from abc import ABC, abstractmethod
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

import csv
import json
import xmltodict as ET
# tree = et.parse('inventory.xml')
# root = tree.getroot()


# REQUISITO 4


class Inventory:
    @classmethod
    # @abstractmethod
    def import_data(cls, data, type):
        if 'csv' in data:
            return cls.open_csv(data, type)
        if 'json' in data:
            return cls.open_json(data, type)
        if '.xml' in data:
            return cls.open_xml(data, type)
        else:
            raise ValueError("Arquivo inválido")

    @classmethod
    def open_csv(cls, data, type):
        with open(data, encoding="utf-8") as file:
            result = list(csv.DictReader(file, delimiter=",", quotechar='"'))
        if (type == 'simples'):
            return SimpleReport.generate(list(result))
        elif (type == 'completo'):
            return CompleteReport.generate(list(result))

    @classmethod
    def open_json(cls, data, type):
        with open(data, mode="r") as file:
            result = json.load(file)
        if (type == 'simples'):
            return SimpleReport.generate(list(result))
        elif (type == 'completo'):
            return CompleteReport.generate(list(result))

    @classmethod
    def open_xml(cls, data, type):
        with open(data) as file:
            result = ET.parse(file.read())['dataset']['record']
        if (type == 'simples'):
            return SimpleReport.generate(list(result))
        elif (type == 'completo'):
            return CompleteReport.generate(list(result))
