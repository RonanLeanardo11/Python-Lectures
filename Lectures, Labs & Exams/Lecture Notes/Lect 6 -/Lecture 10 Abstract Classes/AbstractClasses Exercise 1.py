from abc import ABC, abstractmethod

'Create an abstract class called Shape which has two abstract methods: area and perimeter.
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

'Create a subclass Circle which has one instance variable radius, a constructor which takes
'one parameter which is the radius, and two methods area and perimeter that both return a
'value'
class Circle(Shape):
    Radius = 0


    def __init__(self,Radius_in=0):
        self.Radius = Radius_in

    def area(self): ### Note "area" def name matches abstract method above. has to match this is the rule ** see the arrows pointing to super class **
        Circle_Area = self.Radius * 5
        return Circle_Area

    def perimeter(self): ### Note perimeter def name matches abstract method above. has to match
        Perimeter_Area = self.Radius * 10
        return Perimeter_Area


'Create another subclass Rectangle which has two instance variables length and width, a
'constructor which takes two parameters which is the length and width, and two methods
'area and perimeter that both return a value.

class Rectangle(Shape):
    length = 0
    width = 0

    def __init__(self, length_in, Width_in):
        self.length = length_in
        self.width = Width_in

    def area(self): ### Note "area" def name matches abstract method above. has to match this is the rule
        Rec_Area = self.length * self.width
        return Rec_Area

    def perimeter(self): ### Note perimeter def name matches abstract method above. has to match
        Per_Area = self.length + self.width
        return Per_Area



# In your main program body:
#  Create two Circle objects , radius of 1.0 and 2.5 respectively.
Circle1 = Circle(1.0)
Circle2 = Circle(2.5)


#  Create two Rectangle objects , length and width of 3,4 and 2,2 respectively
Rectangle1 = Rectangle(3,2)
Rectangle2 = Rectangle(4,2)

#  Find and print the sum of the areas of the Rectangle objects
print(sum(Rectangle2.area() + Rectangle2.area()))

#  Find and print the sum of the perimeters of the Circle objects