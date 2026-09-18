class CombinationLock:
    def __init__(self, combination):
        self.combination = combination
        self.status = 'LOCKED'
        self.entered = []

    def enter_digit(self, digit):
        if self.status in ['OPEN', 'ERROR']:
            return

        self.entered.append(digit)

        for i in range(len(self.entered)):
            if self.entered[i] != self.combination[i]:
                self.status = 'ERROR'
                return

        if len(self.entered) == len(self.combination):
            self.status = 'OPEN'
        else:
            self.status = ''.join(str(d) for d in self.entered)

cl = CombinationLock([1, 2, 3, 4, 5])

print(cl.status)  # LOCKED

cl.enter_digit(1)
print(cl.status)  # 1

cl.enter_digit(2)
print(cl.status)  # 12

cl.enter_digit(3)
print(cl.status)  # 123

cl.enter_digit(4)
print(cl.status)  # 1234

cl.enter_digit(5)
print(cl.status)  # OPEN