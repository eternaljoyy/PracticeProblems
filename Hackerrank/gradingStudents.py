import math

def gradingStudents(grades):
	newGrades = []

	for mark in grades: 
		nextMultiple = math.ceil(mark/5)*5 
		if(mark >= 38):
			if(nextMultiple - mark < 3):
				mark = nextMultiple 
				print(mark)
				newGrades.append(mark)
			else:
				#dont round the mark 
				newGrades.append(mark)
		else:
			newGrades.append(mark)
	return newGrades


print(gradingStudents([73, 67, 38, 33]))