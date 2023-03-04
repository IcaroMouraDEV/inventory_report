from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv

class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        with open(path, encoding='utf-8') as file:
            products = csv.reader(file, delimiter=',', quotechar='"')
            header, *data = products
            arr = []
            print(data)
            for index in range(len(data)):
                dict = {}
                for header_index in range(len(header)):
                    dict[header[header_index]] = data[index][header_index]
                arr.append(dict)
            print(arr[0])

        report = SimpleReport if type == 'simples' else CompleteReport

        return report.generate(arr)
