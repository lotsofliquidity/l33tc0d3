def MakeTheStringGreat(s):
	stack = []
	
	# leEeetcode
	# l
	# e
	# E
	# e
	# e
	# t


	# abBAcC
	# a

	for ch in s:
		if stack and stack[-1].lower() == ch.lower() and stack[-1].islower() != ch.islower():
			stack.pop()
			continue
		stack.append(ch)
				
	return "".join(stack)
