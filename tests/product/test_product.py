from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        'arroz',
        'prato fino',
        '15/08/2010',
        '15/12/2010',
        'nz123',
        'local seco longe da luz',
    )

    assert product.id == 1
    assert product.nome_do_produto == 'arroz'
    assert product.nome_da_empresa == 'prato fino'
    assert product.data_de_fabricacao == '15/08/2010'
    assert product.data_de_validade == '15/12/2010'
    assert product.numero_de_serie == 'nz123'
    assert product.instrucoes_de_armazenamento == 'local seco longe da luz'
# Seu teste deve ser escrito aqui
