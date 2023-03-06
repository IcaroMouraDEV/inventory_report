from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path: str, type: str):
        self.data += self.importer.import_data(path)
        report = {'simples': SimpleReport, 'completo': CompleteReport}
        return report[type].generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
