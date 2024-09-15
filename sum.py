def add_two_numbers(num1, num2):
    return num1 + num2

def main():
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Calculate the sum of the two numbers
    result = add_two_numbers(num1, num2)
    
    # Print the result
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()