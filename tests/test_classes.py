import pytest
import unittest
from unittest.mock import patch
from src.classes import Category, LawnGrass, Product, Smartphone, BaseProduct, TestProduct, MixinPrint


@pytest.fixture
def product_sams():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product(product_sams):
    assert product_sams.name == "Samsung Galaxy S23 Ultra"
    assert product_sams.description == "256GB, Серый цвет, 200MP камера"


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category_smart():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни.",
        [product1, product2, product3],
    )


def test_category(category_smart):
    assert category_smart.name == "Смартфоны"
    assert category_smart.description == (
        "Смартфоны, как средство не только коммуникации, но и получения " "дополнительных функций для удобства жизни."
    )
    assert category_smart.category_count == 1
    assert category_smart.product_count == 3


new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_str_product(product_sams):
    assert str(product_sams) == "Samsung Galaxy S23 Ultra, 180000.0 руб., остаток: 5 шт"


def test_add_product():
    assert (product1 + product2) == 2580000.0


def test_str_category(category_smart):
    assert str(category_smart) == "Смартфоны, 27 шт"


def test_new_product() -> None:
    assert new_product.price == 180000


def test_add_product_category(category_smart):
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    Category.add_product(category_smart, product4)
    assert category_smart.product_count == 10


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


def test_smartphone(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.quantity == 5
    assert smartphone1.color == "Серый"
    assert smartphone1.memory == 256
    assert smartphone1.price == 180000.0


@pytest.fixture
def lawngrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_lawngrass(lawngrass1):
    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"


class TestBaseProduct(unittest.TestCase):
    """класс для теста абстракного класса"""

    def test_abstract_class_instantiation_fails(self):
        """Проверка, что нельзя создать экземпляр абстрактного класса"""
        with self.assertRaises(TypeError):
            BaseProduct("Test", "Desc", 100, 5)

    def test_concrete_implementation_works(self):
        """Проверка работы конкретной реализации"""
        product = TestProduct("Laptop", "Gaming laptop", 999.99, 10)

        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "Gaming laptop")
        self.assertEqual(product.price, 999.99)
        self.assertEqual(product.quantity, 10)

    def test_required_attributes_exist(self):
        """Проверка наличия обязательных атрибутов после инициализации"""
        product = TestProduct("Phone", "Smartphone", 699.99, 20)

        # Проверяем, что все атрибуты созданы
        self.assertTrue(hasattr(product, 'name'))
        self.assertTrue(hasattr(product, 'description'))
        self.assertTrue(hasattr(product, 'price'))
        self.assertTrue(hasattr(product, 'quantity'))

    @patch('builtins.print')
    def test_initialization_with_edge_cases(self, mock_print):
        """Тест граничных случаев при инициализации"""
        # Пустые строки
        product1 = TestProduct("", "", 0, 0)
        self.assertEqual(product1.name, "")
        self.assertEqual(product1.price, 0)

        # Отрицательные значения (если допустимо)
        product2 = TestProduct("Negative", "Test", -10, -5)
        self.assertEqual(product2.price, -10)


# if __name__ == '__main__':
#     unittest.main()


@pytest.fixture
def category_mp():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return(Category("Пустая категория с 0", "Категория без продуктов", [product1,product2]))


def test_middle_price(category_mp):
    assert category_mp.middle_price() == 195000.0


# тест ненулевого количества
def test_quantity_zero():
    with pytest.raises(ValueError, match ='Товар с нулевым количеством не может быть добавлен') as e:
        product_zero=Product("Iphone 15", "512GB, Gray space", 0, 0)


#тест миксин
def test_mixin():
    assert repr(product1) == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
