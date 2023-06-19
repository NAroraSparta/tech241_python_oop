class Calculator:
    def __init__(self):
        self.total = 0

    def addition(self, x, y):
         self.total = x + y

    def subtract(self, x, y):
        self.total = x - y

    def multiply(self, x, y):
        self.total = x * y

    def divide(self, x, y):
        self.total = x / y


# Example usage
calc = Calculator()
calc.addition(5, 6)
print(calc.total)  # Output: 0

calc.subtract(11, 6)
print(calc.total)

calc.multiply(3, 5)
print(calc.total)

calc.divide(40, 8)
print(calc.total)


