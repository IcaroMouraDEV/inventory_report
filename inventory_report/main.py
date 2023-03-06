from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    importers = {'csv': CsvImporter, 'json': JsonImporter, 'xml': XmlImporter}

    if len(sys.argv) < 3:
        return print('Verifique os argumentos', file=sys.stderr)

    *trash, path, type = sys.argv

    report = InventoryRefactor(
        importers[path.split('.')[1]]
    ).import_data(path, type)

    print(report, end='')

if __name__ == '__main__':
    main()
