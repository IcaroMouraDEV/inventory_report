from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def __get_most_commom_company(item_list):
        company = Counter(item['nome_da_empresa'] for item in item_list)
        return company.most_common(1)[0][0]

    @staticmethod
    def __get_fab_and_val_date(item_list):
        data_fab = min([item['data_de_fabricacao'] for item in item_list])
        data_validade = min([
            itm['data_de_validade'] for itm in item_list if datetime.strptime(
                itm['data_de_validade'],
                '%Y-%m-%d') > datetime.now()
        ])

        return (data_fab, data_validade)

    @staticmethod
    def generate(item_list) -> str:
        data = SimpleReport.__get_fab_and_val_date(item_list)
        company = SimpleReport.__get_most_commom_company(item_list)
        data_fabricacao, data_validade = data

        return f'''
Data de fabricação mais antiga: {data_fabricacao}
Data de validade mais próxima: {data_validade}
Empresa com mais produtos: {company}
        '''
