import math
import random

def Alpha(num):
    count = 1
    while(count <= num):
        print(count)
        count += 1
def Bravo():
    sum = 0
    for i in range(1, 11):
        sum += i
    return sum
def Charlie(list_of_nums):
    list = []
    for num in list_of_nums:
        cube_root = num ** (1/3)
        list.append(cube_root)
    return list
def Delta():
    while True:
        age = int(input("Enter your age: "))
        if(age >= 0 and age <= 100):
            return age
def Echo():
    nums = []
    for i in range(20):
        nums.append(random.randint(1,100))
    with open("theFile.txt", "w") as file:
        for num in nums:
            file.write(str(num) + "\n")
def Foxtrot(my_float):
    return my_float * 2
def pick_a_color():
    color = str(input("Enter your color: "))
    if color == "blue":
        print("Great choice")
    elif color == "red":
        print("Poor choice")
    elif color == "green":
        print("Not a bad choice")
    else:
        print("Sorry, that's not a primary color")
def randomNumber():
    num = random.randint(1,100)
    if num > 50:
        print(num)
        print("greater than 50")
    else:
        print(num)
        print("less than 50")
def Golf():
    return random.randint(1,6)
def Hotel():
    count = 1
    while True:
        die_1 = Golf()
        die_2 = Golf()
        if die_1 == die_2:
            print("it took this many tries: ", count)
            break
        else:
            count += 1
def India(my_list):
    evens_and_odds = []
    for num in my_list:
        if num % 2 == 0:
            evens_and_odds.append(0)
        else:
            evens_and_odds.append(1)
    return evens_and_odds
def Juliett(my_num):
    return my_num % 2 == 0
def Kilo(my_list):
    half_of_each = []
    for num in my_list:
        half_of_each.append(num / 2)
    with open("theFile.txt", "w") as file:
        for num in half_of_each:
            file.write(str(num) + "\n")

def pay_rate():
    PAY_RATE = 50
    hours_worked = int(input("How many hours worked? "))
    print(hours_worked * PAY_RATE) if hours_worked > 10 else print(0)

# don't understand this one
# def Lima():
def celsuis_and_fahrenheit():
    for i in range(-20,21):
        print(f"Celsuis: {i} \tFahrenheit: {round(i * 1.8 + 32,1)}")

def Fibonacci():
    a = 0
    b = 1
    for i in range(20):
        print(b)
        a, b = b, a + b
def isPrime(number):
    if(number % 2 == 0):
        return False
    else:
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True

def Mike(num):
    return isPrime(num)

def November(grade):
    if 90 <= grade <= 100:
        print("You got an A")
    elif grade >= 80:
        print("You got an B")
    elif grade >= 70:
        print("You got an C")
    else:
        print("You did not pass")

def main():
    November(80)

main()