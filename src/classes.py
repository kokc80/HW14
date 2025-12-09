# класс продукт ветка дев



class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
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
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    def test_new_product():
        new_product.price = 0
        assert new_product.price == 180000
        new_product.price = 12000
        assert new_product.price == 12000


    def __add__(self, other):
        return (self.price*self.quantity + other.price*other.quantity)


    def __str__(self):
        return f"{self.name}', {self.price} руб., остаток: {self.quantity} шт"

class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)


    @property
    def products(self):
        return self.__products


    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


    def __str__(self):
        return f'{self.name}, {self.age} лет'


    new_product = Product.new_product(
        {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        }
    )