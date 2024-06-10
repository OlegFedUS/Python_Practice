pizzas = ["banana", "olives", "pepperoni"]

#4.1

for namesP in pizzas:
    print("I like " + f"{namesP}" + " pizza")
    print("I really love that pizza!\n")

#4.2

animals = ["dog", "cat", "parrot"]

x = 0
for namesA in animals:
    x = range(len(animals) - 1)
    print(namesA + " would be a great pet!")
    if len(x) == 3:
        print("Any of these animals would make a great pet!")

print(x)
