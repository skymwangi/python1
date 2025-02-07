# create a class called fruits that have the following attributes: name,colour and price
# implement a constructor method and a method function that prints:"My favourite fruit is___, colour:___ and costs ____"
# create 5 instances of that class


class Fruits:
    # constructor method
    def __init__(self,name,colour,price):
        self.name=name
        self.colour=colour
        self.price=price
    # a method function
    def favourite_fruit(self):
        print(f"My favourite fruit is {self.name}.\n"
              f"It is {self.colour} in colour.\n"
              f"It costs sh.{self.price}\n")
# create instances of the class
object=Fruits("pineapple","yellow",50)
object.favourite_fruit()

o=Fruits("grapes","purple",100)
o.favourite_fruit()

kinyua=Fruits("orange","orange",25)
kinyua.favourite_fruit()

sky=Fruits("kiwi","green",15)
sky.favourite_fruit()

obj=Fruits("watermelon","red",50)
obj.favourite_fruit()


