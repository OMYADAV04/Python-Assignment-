class MathOperations:
    
    def add(a, b):
        return a + b

    
    def subtract(a, b):
        return a - b

    
    def multiply(a, b):
        return a * b

    
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


class StringOperations:
    
    def concatenate(s1, s2):
        return s1 + s2

    
    def count_characters(string):
        return len(string)

    
    def reverse(string):
        return string[::-1]
    
