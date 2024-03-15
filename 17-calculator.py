class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

def main():
    calc = Calculator()
    
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = int(input("Enter choice (1/2/3/4): "))
    
    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == 1:
            result = calc.addition(num1, num2)
            print("Result:", result)
        elif choice == 2:
            result = calc.subtraction(num1, num2)
            print("Result:", result)
        elif choice == 3:
            result = calc.multiplication(num1, num2)
            print("Result:", result)
        elif choice == 4:
            result = calc.division(num1, num2)
            print("Result:", result)
    else:
        print("Invalid choice")

main()
