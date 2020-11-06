def calculate(number) :
    if number % 2 == 0 :
        number = number / 2
    elif number % 2 == 1 :
        number = number * 3 + 1
    return number

number = 50011
numbers = []
while number != 1 :
    numbers.append(str(int(number)))
    number = calculate(number)

numbers.append(str(int(number)))
output = " -> ".join(numbers)
print(output)