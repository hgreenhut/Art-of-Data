# Practice 
# Create a ComplexNumber class with a constructor method. 
# Write methods for addition, subtraction, multiplication, and division with objects of your ComplexNumber class. 
# Write a str method for your class. What is special about this method? What is the difference between your str method and the default one for your class? 

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __str__(self):
        return str(self.real) + " + " + str(self.imaginary) + "i"
    def addition(self, another_number):
        self.real = self.real + another_number.real
        self.imaginary = self.imaginary + another_number.imaginary
    def subtraction(self, another_number):
         self.real = self.real - another_number.real
         self.imaginary = self.imaginary - another_number.imaginary
    def multiplication(self, another_number):
        newReal = (self.real * another_number.real) - (self.imaginary * another_number.imaginary)
        newImaginary = self.real * another_number.imaginary + another_number.real * self.imaginary
        self.real = newReal
        self.imaginary = newImaginary
    def division(self, another_number):
        newReal = ((self.real * another_number.real) + (self.imaginary * another_number.imaginary))/((another_number.real*another_number.real) + (another_number.imaginary * another_number.imaginary))
        newImaginary = ((self.imaginary * another_number.real) - (self.real * another_number.imaginary))/((another_number.real*another_number.real) + (another_number.imaginary * another_number.imaginary))
        self.real = newReal
        self.imaginary = newImaginary

a = ComplexNumber(5, 6)
b = ComplexNumber(4, 12)
print(a)
print(b)
a.division(b)

print(a)

class CN:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __str__(self):
        if self.imaginary < 0:
            return str(self.real) + " - " + str(-self.imaginary) + "i"
        else:
            return str(self.real) + " + " + str(self.imaginary) + "i"
    def addition(self, another_number):
        return CN(self.real + another_number.real,self.imaginary + another_number.imaginary)
    def subtraction(self, another_number):
        return CN(self.real - another_number.real, self.imaginary - another_number.imaginary)
    def multiplication(self, another_number):
        return CN((self.real * another_number.real) - (self.imaginary * another_number.imaginary), 
        self.real * another_number.imaginary + another_number.real * self.imaginary)
    def conjugate(self):
        return CN(self.real, -self.imaginary)
    #def division(self, another_number):
     #   return CN(self.real.multiplication(another_number.real.conjugate()))
a = CN(5,6)
b = CN(4, 12)

c = a.multiplication(b)
print(a)
print(b)
print(c)
d = c.conjugate()
print(d)