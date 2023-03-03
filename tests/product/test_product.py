from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id = 1,
        nome_da_empresa = 'Moura Hardware Inc',
        nome_do_produto = 'Mouse gamer Moura Mx-9000',
        data_de_fabricacao = '03/03/2023',
        data_de_validade = '03/03/2024',
        numero_de_serie = '000001',
        instrucoes_de_armazenamento = 'Cuidado com a peça usb que conecta o mouse sem fio ao computador',
    )
    print(product)
    assert repr(product) == f'O produto Mouse gamer Moura Mx-9000 fabricado em 03/03/2023 por Moura Hardware Inc com validade até 03/03/2024 precisa ser armazenado Cuidado com a peça usb que conecta o mouse sem fio ao computador.'
