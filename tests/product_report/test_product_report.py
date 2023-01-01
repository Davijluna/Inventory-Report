from inventory_report.inventory.product import Product


def test_relatorio_produto():
    test_self = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        4467254944021,
        "instrucao 1",
    )
    assert str(test_self) == (
            f"O produto {test_self.nome_do_produto}"
            f" fabricado em {test_self.data_de_fabricacao}"
            f" por {test_self.nome_da_empresa} com validade"
            f" até {test_self.data_de_validade}"
            f" precisa ser armazenado {test_self.instrucoes_de_armazenamento}."
        )
