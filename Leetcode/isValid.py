def isValid(s): 
	pattern = {'(': ')', '{': '}', '[': ']'}
	stack = []

	for char in range(len(s)):
		#check the keys of the dictionary
		if (s[char] in pattern):
			#append opening bracket to dictionary
			stack.append(s[char]) 
		else:
			if(len(stack) > 0):
				if (stack[-1] == '(' and s[char] == ')'):
					stack.pop()
				elif(stack[-1] == '{' and s[char] == '}'):
					stack.pop()
				else:
					if(stack[-1] == '[' and s[char] == ']'):
						stack.pop()  
	return len(stack) == 0



print(isValid('()')) 
print(isValid("([)]"))
print(isValid('\\{[]\\}')) 
print(isValid('()[]\\{\\}')) 

