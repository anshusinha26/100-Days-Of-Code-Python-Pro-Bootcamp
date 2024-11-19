"""function with unlimited arguments"""
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

result = add(1, 2, 3, 4, 5)
print(result)

"""*kwargs"""
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(n=2, add=2, multiply=5)