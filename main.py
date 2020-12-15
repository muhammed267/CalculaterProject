print("please enter two  numbers")
print("number one : ")
number1 = input()
print("number two : ")
number2 = input()


def plus(a, b):
    print("Plus : ", int(a) + int(b))


plus(number1, number2)


def minus(a, b):
    print("Minus :", int(a) - int(b))


minus(number1, number2)


def times(a, b):
    print("Times :", int(a) * int(b))


times(number1, number2)


def divide(a, b):
    print("Divide :", int(a) / int(b))


divide(number1, number2)