from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        result = []
        for product in products:
            if product.color == color:
                result.append(product)
        return result

    def filter_by_size(self, products, size):
        result = []
        for product in products:
            if product.size == size:
                result.append(product)
        return result

    def filter_by_size_and_color(self, products, size, color):
        result = []
        for product in products:
            if product.size == size and product.color == color:
                result.append(product)
        return result


# Näidiskasutus
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