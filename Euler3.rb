target = 600851475143
max = Math.sqrt(target).to_i

n = 3

p = []

# define a prime generator
while n < max
	if p.all? { |f| n % f != 0 }
		# if n is a prime
		p << n
		# check if n is a prime factor
		if (target % n == 0)
			target = target / n
			max = Math.sqrt(target).to_i
		end	
	end
	# no need to try the even number
	n += 2
end

print target
