		
		
import math

def gradingStudents(grades):

	newMark = 0 
	newGrades = []

	for mark in grades: 
		nextMultiple = math.ceil(mark/5)*5

		if (mark < 38):
			newGrades.append(mark)
		elif (nextMultiple - mark < 3):
			newMark = nextMultiple
			newGrades.append(newMark)
		else:
			newGrades.append(mark)
	return newGrades

print(gradingStudents([73, 67, 38, 33]))