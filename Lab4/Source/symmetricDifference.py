#Initializing two sets.
s1={1,2,3}
s2={3,4}
print("set 1:",s1,"set 2:",s2)
#Computing s1-s2
s3=s1.difference(s2)
#Computing s2-s1
s4=s2.difference(s1)
#Computing symmetric difference i.e., (s1-s2)Union(s2-s1)
s5=s3.union(s4)
print("symmetric difference:",s5)
