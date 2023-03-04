from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def __get_most_commom_company(item_list):
        company = Counter(item['nome_da_empresa'] for item in item_list)
        return company.most_common(1)[0][0]
    
    @staticmethod
    def __get_fab_and_val_date(item_list):
        data_fabricacao = item_list[0]['data_de_fabricacao']
        data_validade = item_list[0]['data_de_validade']

        for item in item_list:
            if item['data_de_fabricacao'] > data_fabricacao:
                data_fabricacao = item['data_de_fabricacao']

            if (
                data_validade > str(date.today())
                and item['data_de_validade'] < data_validade
            ):
                data_validade = item['data_de_validade']

        return (data_fabricacao, data_validade)

        
    @staticmethod
    def generate(item_list) -> str:
        company = SimpleReport.__get_most_commom_company(item_list)
        data_fabricacao, data_validade = SimpleReport.__get_fab_and_val_date(item_list)

        return f'''
Data de fabricação mais antiga: {data_fabricacao}
Data de validade mais próxima: {data_validade}
Empresa com mais produtos: {company}
        '''


print(SimpleReport.generate([
    {
       "id": 1,
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     }
]))
