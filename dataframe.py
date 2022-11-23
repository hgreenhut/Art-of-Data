# Application 
# Design a DataFrame class to store generic tabular data. 
# Consider how your constructor method should work. 
# What other methods should your class have 
# (or in other words, what other operations do you want to be able 
# to perform on a generic data set)? Implement your class. 

data = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]


class dataframe:
    count = 0
    def __init__(self, data):
        self.data = data
    def length(self):
        for i in self.data:
            self.count = self.count + 1
        return self.count
a = dataframe(data)
print(a)
print(a.length)


