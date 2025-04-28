from resolver import Resolver
from validate import ValidateInput

validator = ValidateInput()
res1 = Resolver()
res2 = Resolver()

number = input("Zadej číslo: ")
number2 = input("Zadej číslo: ")
operation = input("Zadej operaci: ")

[passing, numbers] = validator.validate_numbers([number, number2])
if (not passing):
    print(validator.error_message)
    exit(1)
[passing, operation ]= validator.validate_operation(operation)
if (not passing):
    print(validator.error_message)
    exit(1)

print(numbers, operation)
res1.calculate(numbers, operation)

print(res1.resolve())

