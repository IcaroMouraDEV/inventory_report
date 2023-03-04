import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.split('.')[1] != 'xml':
           raise ValueError('Arquivo inválido')
        with open(path) as file:
            xml = ET.parse(file).getroot()
            return [
                {itm.tag: itm.text for itm in product} for product in xml
            ]
