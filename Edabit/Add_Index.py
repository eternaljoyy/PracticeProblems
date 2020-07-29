def add_indexes(lst):
	newList = [] 
	for index, value in enumerate(lst):
		diffNum = value + index
		newList.append(diffNum)
	return newList 

	