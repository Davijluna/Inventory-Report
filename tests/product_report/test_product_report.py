from inventory_report.inventory.product import Product


def test_relatorio_produto():
    test = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        4467254944021,
        "instrucao 1",
    )
    assert str(test) == (
            f"O produto {test.nome_do_produto}"
            f" fabricado em {test.data_de_fabricacao}"
            f" por {test.nome_da_empresa} com validade"
            f" até {test.data_de_validade}"
            f" precisa ser armazenado {test.instrucoes_de_armazenamento}."
        )
