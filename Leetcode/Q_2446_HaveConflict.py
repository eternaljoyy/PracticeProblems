def haveConflict(event1, event2):
	''' 
	- Figure out how 2 events with times overlap 
	one another 
	- Return True if they overlap, otherwise return False
	'''  

	# check when theres no intersections/conflicts 
	if (event1[1] < event2[0]) or (event2[1] < event1[0]):
		return False 
	return True 


# Tests 
print(haveConflict(["01:15","02:00"], ["02:00","03:00"]))
print(haveConflict(["10:00","11:00"], ["14:00","15:00"]))
print(haveConflict(["14:13","22:08"], ["02:40","08:08"]))