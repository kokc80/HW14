import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


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
    assert (product1 + product2) == 2580000.0


def test_str_category(Category_Smart):
    assert str(Category_Smart) == "Смартфоны, 27 шт"


def test_new_product() -> None:
    assert new_product.price == 180000


def test_add_product_Category(Category_Smart):
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    Category.add_product(Category_Smart, product4)
    assert Category_Smart.product_count == 4


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


def test_Smartphone(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.quantity == 5
    assert smartphone1.color == "Серый"
    assert smartphone1.memory == 256
    assert smartphone1.price == 180000.0


@pytest.fixture
def lawngrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_Lawngrass(lawngrass1):
    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"
