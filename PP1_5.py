'''
  Lesson: Typecasting
  Author: Helen Lin
  Date Created: September 23, 2024
  Date Last Modified: September 23, 2024
'''
def q1():
  #Write Assignment code here
  num = input("Input an integer: ")
  num = int(num)
  num = num + 3
  print(num)

def q2():
  #Write Assignment code here
  num = input("Input a number: ")
  num = num + 4
  num1 = float(num)
  print(num1 + 2)

def q3():
  #Write Assignment code here
  radius = input("Input a radius: ")
  radius = float(radius)
  area = radius * radius
  area = 3.14 * radius
  print(area)
  
def q4():
  #Write Assignment code here
  num = input("Input a number: ")
  num = float(num)
  num = (num * 12)
  num = int(num)
  print(num)

def q5():
  #Write Assignment code here
  num = input("Input an integer: ")
  num = int(num)
  var = num + 5
  print (f"Your number + 5 is: {var}")

#Comment this code out when running tests
#Do not comment this out when running your program normally

#q1()
#q2()
#q3()
#q4()
#q5()
