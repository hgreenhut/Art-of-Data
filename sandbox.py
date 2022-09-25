#
#for i in range(2, 20, 3): 
#    print(i) 

#i = 2
#while i < 20:
#    print(i)
#    i += 3

#def add(a,b):
 #   return a + b

#print(add(7,2))

#def larger(a, b):
 #   if a > b:
  #     return a
   # else:
    #    return b


#print(larger(7,9))
#def xor(a,b):
 #   if a != b:
  #      return True
  #  else:
   #     return False

#print(xor(True, True))

#def hello(n):
 #   for i in range(n):
  #      print("hello")

#hello(7)

#def fraction(x):
 #   print(float(x))

#fraction(1/3)

def factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1, n):
            n = n * i
        return n

print(factorial(5))

# stars(n) prints a right triangle of stars with height and base n ex: stars(3) should print: 
#* 
#** 
#***

def stars(n):
    stars = ""
    for i in range(n+1):
        stars += i * "*"
        stars += "\n"
    print(stars)
    


stars(3)

