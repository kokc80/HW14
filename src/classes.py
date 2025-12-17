from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс - родитель для класса продуктов"""
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

# Тестовый подкласс для проверки
class TestProduct(BaseProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class MixinPrint:
    """Класс-миксин для печати в консоль информации в читаемом виде"""
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """Метод для информативного отображения для отладки"""
        return (
            f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
        )


class Product(BaseProduct, MixinPrint):
    name: str
    description: str
    price: float
    quantity: int
    count_category = 0
    count_product = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        # print(repr(self))

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: int):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data):
        name = product_data.get("name")
        description = product_data.get("description")
        __price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, __price, quantity)

    def __add__(self, other):
        """Сложение двух продуктов по цене и количеству, если оба продукта одного класса"""
        if isinstance(self, Category) is isinstance(other, Category):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError(f"Нельзя добавлять разные продукты: {type(self).__name__} и {type(other).__name__}")
        return self.__price * self.quantity + other.__price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб., остаток: {self.quantity} шт"


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, __products):
        self.name = name
        self.description = description
        self.__products = __products
        Category.category_count += 1
        Category.product_count += len(__products)

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт. \n"
        return product_str

    def add_product(self, product: Product):
        self.product_count += 1
        self.__products.append(product)

    def __str__(self):
        prod_count = 0
        for product in self.__products:
            prod_count += product.quantity
        return f"{self.name}, {prod_count} шт"

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
