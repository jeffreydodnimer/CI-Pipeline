class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        return a ** b

    def mod(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulus by zero.")
        return a % b
    