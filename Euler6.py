#print(abs(reduce(lambda x, y: x+y, map(lambda x: x**2, range(1, 101))) - reduce(lambda x, y: x+y, range(1, 101))**2))
print(abs(sum([x**2 for x in range(1, 101)]) - sum(range(1, 101))**2))
