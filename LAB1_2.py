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

class BetterFilter:
    @staticmethod
    def filter(products, specification):
        return [
            product
            for product in products
            if specification.is_satisfied_by(product)
        ]


class ColorSpecification:
    def __init__(self, color):
        self.color = color

    def is_satisfied_by(self, product):
        return product.color == self.color

    def __and__(self, other):
        return AndSpecification(self, other)


class SizeSpecification:
    def __init__(self, size):
        self.size = size

    def is_satisfied_by(self, product):
        return product.size == self.size

    def __and__(self, other):
        return AndSpecification(self, other)


class AndSpecification:
    def __init__(self, *specifications):
        self.specifications = specifications

    def is_satisfied_by(self, product):
        return all(
            specification.is_satisfied_by(product)
            for specification in self.specifications
        )

    def __and__(self, other):
        return AndSpecification(*self.specifications, other)