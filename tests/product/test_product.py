from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Coca-Cola",
        "Coca-Cola Company",
        "2020-01-01",
        "2020-12-31",
        "123456789",
        "em local seco",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Coca-Cola"
    assert product.nome_da_empresa == "Coca-Cola Company"
    assert product.data_de_fabricacao == "2020-01-01"
    assert product.data_de_validade == "2020-12-31"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "em local seco"
