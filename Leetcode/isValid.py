def containsBrackets(s):
	''' 
	purpose: check if s (sequence of brackets) contain a matching pair 
	of opening and closing brackets. Then, check if we've found all of 
	the matching pairs of paranthesis.

	Assumption: the input will be non-empty string 

	- go through the string 
	- check if the bracket is opening bracket 
	    - if so, then we can add that opening bracket to something

	- check if the bracket is a closing bracket 
	   - get the last opening bracket from where we previously added 
	   it in. 
		- if the opening and closing paranthesis match, we can remove 
		the opening bracket 
		- if the opening and closing paratheiss dont match, we do not 
		need to go through string any further
	'''

	stack = []  

	for i in range(len(s)):
		if(s[i] == ')'):
			if(len(stack) != 0 and stack[-1] == '('):
				#remove the opening bracket 
				stack.pop(-1)
			else:
				return False
		elif (s[i] == '}'):
			if(len(stack) != 0 and stack[-1] == '{'):
				stack.pop(-1) 
			else:
				return False
		elif (s[i] == ']'):
			if(len(stack) != 0 and stack[-1] == '['):
				stack.pop(-1) 
			else:
				return False
		else: 
			stack.append(s[i])
	return len(stack) == 0


print(containsBrackets('()'))
print(containsBrackets('({['))
print(containsBrackets(')[]{}'))
print(containsBrackets('()[]{}'))
print(containsBrackets('([)]'))
print(containsBrackets('()'))