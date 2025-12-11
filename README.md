# HW.14 2025-12-05 
API и библиотека requests

# classes.py
Создан модуль classes.py содержит классы
class Product:
    name: str
    description: str
    price: float
    quantity: int 
class Category:
    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0
в классе Сategory category_count и  product_count вычисляются при инициализации 

