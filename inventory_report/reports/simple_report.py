from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(item_list) -> str:
        # https://realpython.com/python-counter/
        company = Counter(item['nome_da_empresa'] for item in item_list)
        data_fabricacao = item_list[0]['data_de_fabricacao']
        data_validade = item_list[0]['data_de_validade']

        for item in item_list:
            if item['data_de_fabricacao'] > data_fabricacao:
                data_fabricacao = item['data_de_fabricacao']

            if data_validade > str(date.today()):
                data_validade = item['data_de_validade']

            # print(data_validade > str(date.today()))
        return f'''
Data de fabricação mais antiga: {data_fabricacao}
Data de validade mais próxima: {data_validade}
Empresa com mais produtos: {company.most_common(1)[0][0]}
        '''
