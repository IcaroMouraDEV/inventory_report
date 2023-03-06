from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter

def test_decorar_relatorio():
    path = 'inventory_report/data/inventory.csv'
    products = CsvImporter.import_data(path)
    colored_simple_report = ColoredReport(SimpleReport).generate(products)
    colored_complete_report = ColoredReport(CompleteReport).generate(products)
    color_codes = ["\033[31m", "\033[32m", "\033[36m"]

    for color_code in color_codes:
        assert (color_code in colored_simple_report) is True
        assert (color_code in colored_complete_report) is True
