from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv

class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        with open(path) as file:
            reader = list(csv.DictReader(file))

            report = SimpleReport if type == 'simples' else CompleteReport

            return report.generate(reader)

print(Inventory.import_data('inventory_report/data/inventory.csv', 'simples'))
