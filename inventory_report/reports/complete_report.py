from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def _count_company_items(list):
        company = Counter(item['nome_da_empresa'] for item in list)
        add_info = ''

        for name, qtd in company.items():
            add_info += f'- {name}: {qtd}\n'
        
        return f'Produtos estocados por empresa:\n{add_info}'

    @classmethod
    def generate(cls, item_list) -> str:
        simple_report = super().generate(item_list)
        add_report_info = cls._count_company_items(item_list)
        return simple_report + '\n' + add_report_info

