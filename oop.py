# object oriented programmimg
class Car:
    # constructor method
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    # a method function
    def describe_car(self):
        print(f"My dream car make: {self.make}\n" 
              f"My dream car model: {self.model}\n"
              f"Manufacturer: {self.year}\n")
# create object or instances of a class
my_object=Car("Toyota","Lexus",2023)
my_object.describe_car()

object2=Car("Audi","Audi SQ5",2007)
object2.describe_car()

myobject=Car("Fiat","Fiat 600e",2024)
myobject.describe_car()

object4=Car("Jeep","Wagon",2021)
object4.describe_car()

obj=Car("Toyota","Corona",1970)
obj.describe_car()
