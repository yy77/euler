import itertools

def fib():
	i,j = 1,1
	while True:
		i,j = j, i+j
		yield i
		
print(sum(filter(lambda x: x%2==0,itertools.takewhile(lambda x: x < 4000000, fib()))))
