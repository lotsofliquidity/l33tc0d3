brackets = {'(': ')', '[': ']', '{': '}'}

def ValidParentheses(input):
	stack = []
		
	
	# input = "()[]{}"
	for parenthese in input:
		if parenthese in brackets:
			stack.append(parenthese)
		else:
			if not stack:
				return False
		
			previous_opening = stack.pop()
			if brackets[previous_opening] != parenthese:
				return False
	return not stack		


		# check for if it's a opening or closing backet
