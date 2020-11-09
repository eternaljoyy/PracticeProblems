def isValid(s):
	stack = []

	for i in range(len(s)):
		if(s[i] == ')'):
			if(stack and stack[-1] == '('):
				stack.pop(-1)
			else:
				return False 
		elif (s[i] == '}'):
			if(stack and stack[-1] == '{'):
				stack.pop(-1)
			else:
				return False 
		elif (s[i] == ']'):
			if(stack and stack[-1] == '['):
				stack.pop(-1)
			else:
				return False 
		else:
			stack.append(s[i])
	return len(stack) == 0

print(isValid('()'))
print(isValid('({['))
print(isValid(')[]{}'))
print(isValid('()[]{}'))
print(isValid('([)]'))