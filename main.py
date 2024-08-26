#Assignment-3 write programs
#Question#1
#Calculate your age based on the current year and your birth year.
print("Age Calculator")
#birth year
birth_year:int =int(input("Enter your birth year= "))
#current year
current_year:int = int(input("Enter your current year= "))
# Output the age
print("Your Age is=" ,(current_year-birth_year))

#Question#2
#Write a program that calculates the area of a rectangle using length and width variables.
print("Rectangular Area Calculator")
#length of rectangle
length:int=int(input("Enter the length of the rectangle= "))
#length of width
width:int=int(input("Enter the width of the rectangle= "))
#output the area
print("The Area of Rectangle is=",(length*width))

#Question#3
#Write a program that calculates the area of a circle.
print("Circle Area Calculator")

#radius
radius:int  = int(input("Enter the radius of cirlce = "))
#value of pie
pie:float= 3.14159
#output the area
print("The Area of the Circle is=",pie*radius**2)

#Question#4
#Write a program that calculates the area of the cube.
print("Cube Area Calculator")
value:int=6
#number of sides
sides=int(input("Enter the number of sides="))
#output the area
print("The Area of Cube is=",value*sides**2)

#Question#5
# Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
print("Temperature Converter From Farenheit To Celsius")
#temperature in farenheit
temperature = int(input("Enter your temperature in Fahrenheit = "))
#temperature in celsius
print("Temperature in Celsius =",(temperature-32)*5/9)

print("Temperature Converter From Celsius To Farenheit")
#temperature in celsius
temperature = int(input("Enter your temperature in celsius = "))
#temperature in farenheit
print("Temperature in Fahrenheit is =", (temperature*9/5)+32)
#Question#6
#Convert a given number of seconds into minutes and seconds using variables.
print("Time Converter From Second To Minutes")
#time in seconds
seconds=float(input("Enter your time in seconds="))
#time in minutes
print("Time in Minutes=",(seconds/60))
print("Time Converter From Minutes To Second ")
#time in minutes
timeminutes = int(input("Enter your time in minutes = "))

print("Time in seconds is =", (timeminutes*60))
#Question#7
#Write a program that calculates the percentage.
print("Percentage Calculator")
obtainedmarks:int= int(input("Enter your obtained marks = "))
totalmarks:int= int(input("Enter your  total marks = "))
print("Percentage is =", (obtainedmarks /totalmarks)*100  )
#Question#8
#Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.
print("BMI Calculator")
weight:int = int(input("enter weight in kilogram = "))
height :int= int(input("enter height in meters = "))
result= weight/height**2
print("result")

   #Question#9
   #Write a program that calculates the volume of a cylinder using the formula .
print("Cylinder Volume Calculator")
radius:int= int(input("Enter the radius of cylinder = "))
height:int = int(input("Enter the height of cylinder =  "))
pie:float = 3.141592653589793238462643383279502884197
print("Volume of Cylinder is =" , pie*(radius**2)*height)