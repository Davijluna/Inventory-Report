from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, file):
        data_de_fabricacao = [item["data_de_fabricacao"] for item in file]
        data_de_fabricacao.sort()
        data_de_validade = [item["data_de_validade"] for item in file]
        data_de_validade.sort()
        empresas_com_mais_produtos = [item["nome_da_empresa"] for item in file]
        empresa = Counter(empresas_com_mais_produtos).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {min(data_de_fabricacao)}\n"
            f"Data de validade mais próxima: {min(data_de_validade)}\n"
            f"Empresa com mais produtos: {empresa}"
        )
