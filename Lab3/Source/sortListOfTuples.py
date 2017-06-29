import operator

#initialize a list
list1=[(1,2),(3,4),(6,3,5),(2,1)]

'''sort is given a parameter called key, to tell it to perform sort 
on key and we are using itemgetter method of operator package
for that purpose.'''
list1.sort(key=operator.itemgetter(-1))

#print sorted list
print(list1)
