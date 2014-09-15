class LCM:
	def gcd (a,b):
		while b:
			a, b = b, a % b
		return a

	def lcm (a,b):
		return a * b // LCM.gcd (a,b)

	def lcmm (args):
		if (len(args) == 2):
			return LCM.lcm (args[0], args[1])

		a = args.pop(0)
		return LCM.lcm (a, LCM.lcmm(args))