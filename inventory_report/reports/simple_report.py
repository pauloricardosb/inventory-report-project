from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def companies_counter(cls, inventory):
        companies = [product["nome_da_empresa"] for product in inventory]
        return Counter(companies)

    @classmethod
    def generate(cls, inventory):
        dates = [product["data_de_fabricacao"] for product in inventory]
        oldest_dates = sorted(dates)[0]

        today_date = str(date.today())
        expiration_dates = [
            product["data_de_validade"]
            for product in inventory
            if product["data_de_validade"] >= today_date
        ]
        closest_dates = sorted(expiration_dates)[0]

        companie_most_products = cls.companies_counter(
            inventory
        ).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_dates}\n"
            f"Data de validade mais próxima: {closest_dates}\n"
            f"Empresa com mais produtos: {companie_most_products}"
        )
