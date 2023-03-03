from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    nome_da_empresa = 'Moura Hardware Inc'
    nome_do_produto = 'Mouse gamer Moura Mx-9000'
    data_de_fabricacao = '03/03/2023'
    data_de_validade = '03/03/2024'
    numero_de_serie = '000001'
    instrucoes_de_armazenamento = 'Cuidado com a peça usb que conecta o mouse sem fio ao computador'
    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert product.id == id
    assert product.nome_do_produto == nome_do_produto
    assert product.nome_da_empresa == nome_da_empresa
    assert product.data_de_fabricacao == data_de_fabricacao
    assert product.data_de_validade == data_de_validade
    assert product.numero_de_serie == numero_de_serie
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento
