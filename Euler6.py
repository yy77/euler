print(abs(reduce(lambda x, y: x+y, map(lambda x: x**2, range(1, 101))) - reduce(lambda x, y: x+y, range(1, 101))**2))
