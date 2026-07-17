# recursion is basically
# Divide: divide the problems into smaller sub-problems
# conquer: Recursively solve those sub problems using simple algo's
# combine: comvine the answers of sub problems to produce the solution of the initial problem

# each recursive algo has to have a base case, and a recursive case

def kPower2(k):
	if k == 0:
		return 1
	else:
		return 2*kPower2(k-1)

print(kPower2(5))

