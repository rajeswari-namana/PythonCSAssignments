#importin pi function
from math import pi

#declaring radius of circle
radiusString=input("enter the radius:")
r=int(radiusString)

#calculating area and circumference
area= pi*r*r
circumference=2*pi*r

#printing the output
print("area: ",area)
print("circumference:",circumference)
