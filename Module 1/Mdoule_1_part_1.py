def addNums(number1,number2):
    return number1 + number2
def subNums(number1, number2):
    return number1 - number2



def main():
    print("The folling program will add and subtract two numbers you provide.\n")
    print("Please provide the first number:", end=" ")
    num1 = int(input())
    print("Please provide the Second number:", end=" ")
    num2 = int(input())
    print(f"\nAdding {num1} to {num2} produces a sum of: {addNums(num1,num2)}")
    print(f"Subtracting {num2} from {num1} produces a value of: {subNums(num1,num2)}\n")

if __name__ == "__main__":
    main()