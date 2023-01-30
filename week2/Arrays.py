cars = ["Ford", "Volvo", "BMW"]
print(cars)
cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)
cars[0] = "Toyota"
print(cars[0])

x = len(cars)
print(x)

for x in cars:
    print(x)

cars.append("Honda")
for x in cars:
    print(x)


cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)
cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)
