#!/usr/bin/env python
# coding: utf-8

# # ex1

name = input ("Enter your name :")
surname = input ("Enter your surname :")
string_print = f"Your name is {name} and your family is {surname }."
print (string_print)


# ex2
i = 1
x = ""
while i < 6:
    film = input("Enter name of your favorite film :")
    x = film + ',' + x + '  '
    print(x)
    i += 1





# ex3

def printfirstlast():
  color_list = ["Red","Green","White" ,"Black"]
  print(color_list[0])
  print(color_list[-1])




printfirstlast()


# ex4

mydictis = {
  0: 10,
  1: 20
}


mydictis[2]=30


mydictis


# ex5

def body():
    weight = input ("Enter weight (kg) :")
    height = input ("Enter weight (m) :")
    bmi = float(weight) / float(height)**2
    print(bmi)


body()






# ex6


i = 1
while i == 1:
  inputNumber = input ("Your guess :")
  print(inputNumber)
  if inputNumber == "6":
    print("Well guessed!")
    break
#  inputNumber = input ("Your guess :")


# ex6 again


def guessNum():
    i= 1
    while i == 1:
        inputNumber = input ("Your guess :")
        print(inputNumber)
        if inputNumber == "6":
            print("Well guessed!")
            break
        else:
            print("Try again")
            continue





guessNum()


# ex7


mytuple = tuple((54, "BMW", 123, "apple", True,False))
print(mytuple)


# ex8


myList = ["Isfahan", "Tehran", "Tabriz","Mashhad","Karaj"]
M = len(myList)
tupleX = tuple()
for x in myList:
    tupleX +=  x,
    print(tupleX)







# ex9


a = [10,20,30,20,10,50,60,40,80,50,40]
newList = []
for x in a:
    if len(newList) == 0:
        newList.append(x)

    else:
        b = 0
        for y in newList:
            b = b + 1
            if y == x:
                b = b - 1
            if y != x and b == len(newList):
                newList.append(x)

print(newList)


# ex10
name = input("enter your text :")


print(len(name))

i = 0
x = ""
while i < len(name):
    if(i%2) == 0:
        print (name[i])
        x = x + name[i]
        i += 1
    else:
        i += 1
        continue
print(x)

