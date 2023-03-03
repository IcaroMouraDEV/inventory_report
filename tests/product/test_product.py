from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_da_empresa='Moura Inc',
        nome_do_produto='Mouse Mx-9000',
        data_de_fabricacao='03/03/2023',
        data_de_validade='03/03/2024',
        numero_de_serie='000001',
        instrucoes_de_armazenamento='Cuidado com usb',
    )

    # https://www.programiz.com/python-programming/methods/built-in/repr
    str = 'O produto Mouse Mx-9000 fabricado em 03/03/2023 por Moura Inc com'
    str2 = 'validade até 03/03/2024 precisa ser armazenado Cuidado com usb'

    assert repr(product) == f'{str} {str2}.'
