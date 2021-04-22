#ex1

import numpy as np
def  fizz_buzz():
    while True:
        try:
            a = input("Input the you desire number")
            a = int(a)
            c = np.divmod(a,3)
            d = np.divmod(a,5)
            if c[1] == 0 and d[1] == 0:
                    print ("FizzBuzz")
            elif c[1]==0:
                    print ("Fizz")
            elif d[1]==0:
                    print ("Buzz")
            else:
                    print(a)
                    
        except ValueError as err:
            print(err)
            break
            
  
fizz_buzz()


# ex2 
def  avoidIndexError():
    lst= [5, 10, 20]
    while True:
        try:
            a = input("Input your desire index:")
            a = int(a)
            b = lst[a]
            string_print = f"Your index is {a} and your value is {b}."
            print(string_print)
        except IndexError as err:
            print(err)
            break
			
avoidIndexError()






#ex3

class Jetinventory():
    def __init__(self, name, country):
        self.name = name
        self.country = country
    a = 4
    b = 5

classInstance = Jetinventory("Afshin", "Iran")

print(classInstance.a)

print(classInstance.name)

print(classInstance.b)

print(classInstance.country)

#ex4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("F:/Class 09/Afshin/iris.csv") 

df.head()
df.isnull()
df.describe()

df.shape

df.info()


viz = df[['sepal_length','sepal_width','petal_length','petal_width']]
viz.hist()
plt.show()

df['species'].value_counts()

g = sns.pairplot(df, hue='species', markers='*')
plt.show()


#ex5 
capitals = {"Germany":"Berlin","Iran":"Tehran","Iraq":"Baqdad","Italy":"ROME",
    "USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}
while True:
    key = input("enter your desire country :")
    key = key.capitalize()
    try:
        print(capitals[key])
    except KeyError as e:
        print('name of this country is not exist in database  -  "%s"' % str(e))
        break
		
		
#ex6
def showNumbers():
    desireNumber = int(input("Input your desire number = "))
 #   desireNumber = (desireNumber)
    for i in  range(desireNumber + 1):
        if (i % 2) == 0:
            print(f" {i} is even")
        else:
            print(f" {i} is odd ")
    

showNumbers()		

#ex7
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv("F:/Class 09/Afshin/creditcard.csv") 
df.head(5)

df.shape

df.isnull()


df.describe()



df.info()


df['Class'].value_counts()

#ex8
class Person:
    def __init__(self,  firstname,  lastname):
        self.firstname = firstname
        self.lastname = lastname
    def name(self):
        print(self.firstname)
        return self.name



ali = Person('afshin','monfared')


ali.name()

#ex9
while True:
    inputNumber = input("Input your number :")
    try:
        i = int(inputNumber)
        print(f"Your number is {i}.")
    except ValueError as err:
        print("you must type number but not character!")
        continue
			
#ex10

class Student:
    pass

class  Marks:
    pass

afshin = Student()
afshinMark = Marks()
hamidMark = Marks()
print(isinstance(afshin,Student))
print(isinstance(hamidMark,object))
print(isinstance(afshinMark,object)) 

