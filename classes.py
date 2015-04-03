__author__ = 'sereg'
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a %s %s with %i MPG." % (self.color, self.model, self.mpg)
    def drive_car(self):
        self.condition = "used"


car1 = Car("DeLorean", "silver", 88)
print car1.condition
print car1.display_car()
#print my_car.model
#print my_car.color
#print my_car.mpg

#print my_car.condition
car1.drive_car()
print car1.condition
class ElectricCar(Car):
    def __init__(self, battery_type):
        self.battery_type = battery_type
    def drive_car(self):
        self.condition = "like new"
    def display_car(self):
        return "This is an Electic %s %s with %i MPG. And a battery type is %s" % (self.color, self.model, self.mpg, self.battery_type)
my_car = ElectricCar("molten salt")
print my_car.battery_type
#my_car = Car("Polo","Red", 88)
my_car.model = "Polo"
my_car.color = "red"
my_car.mpg = 88
print my_car.condition
my_car.drive_car()
print my_car.condition
print my_car.display_car()
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
my_point = Point3D(1, 2, 3)
print my_point