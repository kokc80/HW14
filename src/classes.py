# класс продукт ветка дев
class Product:
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
        self.category_count += 1
        self.product_count += len(__products)

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
        return f"{self.name}, {self.product_count} шт"

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
