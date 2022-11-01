name = input("What is your name? ")
age = input("What is your age? ")
age = int(age)
print("Hello {}, your age is {}".format(name, age))
if age >= 21:
    print("You can buy an alcoholic beverage")
elif age == 20:
    print("One more year")
elif age == 19:
    print("Two more years")
else:
    print("You cannot buy and alcoholic beverage")
