 # Examples
# if-elif-else statement ==, <, >
x = 8
if x < 5:
    print("x is less than 5")
elif x < 10:
    print("x is between 5 and 9")
else:
    print("x is greater than or equal to 10")

# input types
birth_year = input('Birth year: ')
age = 2023 - int(birth_year)
print(age)

# operation PEMDAS  **exponent
x = (2 + 3) * 4 / 2 ** 2 - 1
y = int(x)
print(y)

# while loop with break statement
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1