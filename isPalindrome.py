def isPalindrome(str): 
	''' output -> true/fase (true if string is palindrome)

	- anything alphanumeric is valid 
	- we are ignoring cases (uppercase/lowercase) 
	- special characters (ex: ,  ?   spaces, tabs) 
	    - not taken into consideration

	edge cases
	1) len(str) == 1 
	
	method 1):  
	 - originalStr = '' 
	    - loop through the string 
	       - checking for alphanumeric characters, if true 
	       then add to originalStr; if false, then just continue looping 
	 -  make an extra data structure (ex: list) newArr
	 -  loop through the entire string (backwards) 
	    - check if character is alphanumeric 
		   
	       - if true, then add it to the newArr 
	 - secondStr = ''.join(newArr)
	 - check if string == secondStr
	 - loop through the string 
	''' 
	
	# for i in range(len(str)):



isPalindrome("Programcreek is awesome")
isPalindrome("Red rum, sir, is murder")