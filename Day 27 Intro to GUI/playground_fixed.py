def add(*numbers):
    """Return the sum of any number of numeric arguments."""
    return sum(numbers)


def calculate(number, *, add_amount, multiply_by):
    """Add a value to number, then multiply the result."""
    return (number + add_amount) * multiply_by


class Car:
    def __init__(self, make, model, color, seats=None):
        self.make = make
        self.model = model
        self.color = color
        self.seats = seats


print(add(3, 2, 3, 5, 2, 33))
print(calculate(5, add_amount=4, multiply_by=4))

my_car = Car(make="Nissan", model="Skyline", color="blue", seats=5)
