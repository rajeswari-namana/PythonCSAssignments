#Taking input from user.
t=input("Enter text separated by commas: ")
#splitting words separated by commas which are automatically stored as a list.
l=t.split(",")
#sorting the list.
l1=sorted(l)
#iterating through sorted list and printing output.
for i in l1[:-1]:
    print(i+",",end='')
print(l1[-1])








