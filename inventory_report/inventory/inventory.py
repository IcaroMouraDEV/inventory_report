import csv
import json
import xml.etree.ElementTree as ET

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        data_type = path.split('.')[1]
        with open(path) as file:
            if data_type == 'csv':
                data = list(csv.DictReader(file))
            if data_type == 'json':
                data = json.load(file)
            if data_type == 'xml':  # https://docs.python.org/3/library/xml.etree.elementtree.html
                xml = ET.parse(file).getroot()
                data = [
                    {item.tag: item.text for item in product} for product in xml
                ]
            
            report = SimpleReport if type == 'simples' else CompleteReport

            return report.generate(data)

print(Inventory.import_data('inventory_report/data/inventory.csv', 'simples'))
