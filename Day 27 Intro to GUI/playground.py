def add(*args):
    print(args)
    total = 0
    for n in args:
        total += n
    return total
print(add(3,2,3,5,2,33))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(5 ,add=4, multiply=4)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seat = kw.get("seat")

my_car = Car(make="nissan" , color="skyline" , model= 2019)
