import math


def compound_interest():
    interest_rate = int(input("Enter the interest rate: "))
    principal = int(input("Enter the principal: "))
    num_years = int(input("Enter the number of years: "))
    final_amount = principal * ((1 + interest_rate/100) ** num_years)
    print(f"The final amount will be: {final_amount}")

def age_verification():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            break
    for i in range (3):
        age = input("Enter your age: ")
        if age.isdigit() and int(age) >= 1 and int(age) <= 100:
            print("acceptable")
            break
        if i == 2:
            print("unacceptable")

def password_validation():
    while True:
        password = input("Enter your password: ")
        if (len(password) < 8):
            print("password must be at least 8 characters long")
        elif not any(char.isdigit() for char in password):
            print("password must contain a digit")
        elif not any(char.isupper() for char in password):
            print("password must contain an uppercase letter")
        elif not any(char.islower() for char in password):
            print("password must contain a lowercase letter")
        elif not any(not char.isalnum() for char in password):
            print("password must contain a special character")
        else:
            print("password is acceptable")
            break
def contains_three():
    my_str = "3"
    for i in range(4,1000):
        if any(char == '3' for char in str(i)):
            my_str = my_str + "| " + str(i) + " "
    print(my_str)

def even_numbers_from_100_backwards():
    my_str = "100"
    for i in range(98, 0, -2):
        my_str = my_str + ", " + str(i)
    print(my_str)


def primeNums():
    primes = "101"
    for i in range(102, 1000):
        if isPrime(i):
            primes = primes + ", " + str(i)
    print(primes)


def isPrime(number):
    if(number % 2 == 0):
        return False
    else:
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True
def main():
    # compound_interest()
    # age_verification()
    # password_validation()
    # contains_three()
    # even_numbers_from_100_backwards()
    primeNums()



main()