from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, file):
        report = super().generate(file)
        empresas_com_mais_produtos = [item["nome_da_empresa"] for item in file]
        estocados_por_empresa = Counter(empresas_com_mais_produtos)
        report += "\n Produtos estocados por empresa:\n"
        for inc, quantidades in estocados_por_empresa.items():
            report += f"- {inc}: {quantidades}\n"

        return report
