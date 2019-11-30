class Car:
	def __init__(self,make, model, year,odometer=0,fuel=70):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = odometer
		self.fuel = fuel
	def drive(self):
		global distance
		distance=int(input("How many kilometers will you drive?:"))


	def __subtract_fuel(self):
		global petrol
		petrol=self.fuel-distance
		if petrol<=0:
			print(0)
		else:
			print(petrol)
		if petrol>0:
			print("Let's drive!")
		else:
			print("Need more fuel, please, fill more!")

	def __add_distance(self):
		if distance%self.fuel>=0:
			odometer = self.odometer+distance
			if petrol>=0:
				print(odometer,' km our car drove')



auto = Car('Tesla','Tesla Model X Crossover',2015,10)
auto.drive()
auto._Car__subtract_fuel()
auto._Car__add_distance()
