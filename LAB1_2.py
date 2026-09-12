from enum import Enum

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

class Size(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    
class ProductFilter:
    @staticmethod
    def filter_by_color(products, color):
        return [product for product in products if product.color == color]

    @staticmethod
    def filter_by_size(products, size):
        return [product for product in products if product.size == size]

    @staticmethod
    def filter_by_size_and_color(products, size, color):
        return [product for product in products if product.size == size and product.color == color]


products = [
   Product("Apple", Color.GREEN, Size.SMALL),
   Product("Tree", Color.GREEN, Size.LARGE),
   Product("House", Color.BLUE, Size.LARGE)
]

pf = ProductFilter()

print("Green products:")
for p in pf.filter_by_color(products, Color.GREEN):
   print(p.name)

print("Large blue products:")
for p in pf.filter_by_size_and_color(products, Size.LARGE, Color.BLUE):
   print(p.name)


