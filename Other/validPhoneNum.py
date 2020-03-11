#module that can be used to work with regex
import re

class validPhoneNum: 
	#Return true if phone number is valid, else return false. 
	def validPhoneNum(phoneNum):
		#regex expression for phone number 
		#TODO: make sure of the proper order
		pattern = '\d{3}-\d{3}-\d{4}'

		#check if user input matches the pattern 
		if(re.search(pattern, phoneNum)):
			return True 
		else: 
			return False   


	print(validPhoneNum('416-679-3838'))
	#NOTE: Supposed to return false here...
	print(validPhoneNum('%&^87892'))