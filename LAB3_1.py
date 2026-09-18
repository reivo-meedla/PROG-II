import random


class Generator:
    def generate(self, count):
        return [random.randint(1, 9) for _ in range(count)]


class Splitter:
    def split(self, matrix):
        size = len(matrix)
        result = []

        result.extend(matrix)

        for c in range(size):
            result.append([matrix[r][c] for r in range(size)])

        result.append([matrix[i][i] for i in range(size)])
        result.append([matrix[i][size - 1 - i] for i in range(size)])

        return result


class Verifier:
    def verify(self, sub_lists):
        if not sub_lists:
            return False

        target_sum = sum(sub_lists[0])
        return all(sum(lst) == target_sum for lst in sub_lists)


class MagicSquareGenerator:
    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()

    def generate(self, size):
        while True:
            numbers = self.generator.generate(size * size)

            square = []
            for i in range(0, len(numbers), size):
                square.append(numbers[i: i + size])

            parts = self.splitter.split(square)

            if self.verifier.verify(parts):
                return square


if __name__ == "__main__":
    gen = MagicSquareGenerator()
    square = gen.generate(3)

    for row in square:
        print(row)