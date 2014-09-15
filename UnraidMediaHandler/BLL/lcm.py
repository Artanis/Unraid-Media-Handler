def gcd (a,b):
	while b:
		a, b = b, a % b
	return a

def lcm (a,b):
	return a * b // gcd (a,b)

def lcmm (args):
	if (len(args) == 2):
		return lcm (args[0], args[1])

	a = args.pop(0)
	return lcm (a, lcmm(args))
