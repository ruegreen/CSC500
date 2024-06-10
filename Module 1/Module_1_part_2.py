def multiplyNums(number1,number2):
    return number1 * number2
def divideNums(number1, number2):
    return number1 / number2

def main():
    print("The folling program will multiple and divide two numbers you provide.\n")
    print("Please provide the first number:", end=" ")
    num1 = int(input())
    print("Please provide the Second number:", end=" ")
    num2 = int(input())
    print(f"\nMultiplying {num1} by {num2} produces a value of: {multiplyNums(num1,num2)}")
    print(f"Dividing {num1} by {num2} produces a value of: {divideNums(num1,num2)}\n")

if __name__ == "__main__":
    main()