#Initializing a dictionary d.
d=[{'course': "Python", 'LastGPA' : 90, 'CurrentGPA' : 100},
   {'course': "WebApp", 'LastGPA' : 95, 'CurrentGPA' : 85},
   {'course': "Crypt1", 'LastGPA' : 100, 'CurrentGPA': 100}]
#looping through dictionary
for i in d:
    #popping out two key-value pairs
    LGPA=i.pop('LastGPA')
    CGPA = i.pop('CurrentGPA')
    #inserting a new key-value pair
    i['LastGPA + CurrentGPA'] = int((LGPA + CGPA)/2)
print(d)




