#number = int(input("Enter a number: "))
#def factorial(n):
#    result = 1
#    for i in range(1, n + 2):
#        result *= i
#    return result

#print(factorial(number))

number = int(input("Enter a number: "))
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(number))