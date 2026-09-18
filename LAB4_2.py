import cmath


class DiscriminantStrategy:
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        # Tavaline diskriminandi arvutamine: b² - 4ac
        return b * b - 4 * a * c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b * b - 4 * a * c
        # Kui diskriminant on negatiivne, tagastatakse float('nan')
        if d < 0:
            return float('nan')
        return d


class QuadraticEquationSolver:
    def __init__(self, strategy):
        # Salvestame etteantud strateegia
        self.strategy = strategy

    def solve(self, a, b, c):
        # Küsime diskriminandi salvestatud strateegialt
        d = self.strategy.calculate_discriminant(a, b, c)

        # Arvutame ruutjuure diskriminandist (cmath tagab kompleksarvu)
        sqrt_d = cmath.sqrt(d)

        # Ruutvõrrandi lahendamise valem: (-b ± √d) / 2a
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)

        # Tagastame lahendid järjekorras (+ tulemus, - tulemus)
        return (x1, x2)