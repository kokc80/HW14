import pytest

from src.classes import Category, Product


@pytest.fixture
def product_Sams():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product(product_Sams):
    assert product_Sams.name == "Samsung Galaxy S23 Ultra"
    assert product_Sams.description == "256GB, Серый цвет, 200MP камера"


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def Category_Smart():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни.",
        [product1, product2, product3],
    )


def test_category(Category_Smart):
    assert Category_Smart.name == "Смартфоны"
    assert Category_Smart.description == (
        "Смартфоны, как средство не только коммуникации, но и получения " "дополнительных функций для удобства жизни."
    )
    assert Category_Smart.category_count == 1
    assert Category_Smart.product_count == 3


new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_str_product(product_Sams):
    assert str(product_Sams) == "Samsung Galaxy S23 Ultra, 180000.0 руб., остаток: 5 шт"


def test_add_product() -> None:
    product1 + product2 == 2580000.0


def test_str_category(Category_Smart):
    assert str(Category_Smart) == "Смартфоны, 3 шт"


def test_new_product() -> None:
    assert new_product.price == 180000
