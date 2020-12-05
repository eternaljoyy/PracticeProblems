class ParkingSystem:
	def __init__(self, big, medium, small):
		''' below represent the number of available spots for each parking space'''
		self.big = big
		self.medium = medium 
		self.small = small
		#list containing number of parking spots for each car
		self.parkingSpots = [self.big, self.medium, self.small]

	def addCar(self, carType):
		if (carType == 1):
			if(self.parkingSpots[0] != 0):
				self.parkingSpots[0] -= 1
				return True
			else:
				return False
		elif (carType == 2):
			if(self.parkingSpots[1] != 0):
				self.parkingSpots[1] -= 1
				return True
			else:
				return False
		else:
			if (carType == 3):
				if(self.parkingSpots[2] != 0):
					self.parkingSpots[2] -= 1
					return True
				else:
					return False

	def getBigSpots(self):
		return self.big 

	def getMediumSpots(self):
		return self.medium 

	def getSmallSpots(self):
		return self.small 

	def getParkingSpots(self):
		return self.parkingSpots


parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))   
print(parkingSystem.addCar(2))
print(parkingSystem.addCar(3))
print(parkingSystem.addCar(1))
print(parkingSystem.addCar(2))

parkingSystem2 = ParkingSystem(2, 2, 0)
print(parkingSystem2.addCar(1))
print(parkingSystem2.addCar(1))
print(parkingSystem2.addCar(1))
print(parkingSystem2.addCar(2))
print(parkingSystem2.addCar(2))
print(parkingSystem2.addCar(2))
print(parkingSystem2.addCar(3))
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)