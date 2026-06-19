print("\n______________________________SET DATA_STRUCTUES____________________________________")
print("_______________1.creating________________")
print("\n______A.empty set_______\n")
s={}
print(s)
print(type(s)) #it is dict bcos dict have high value than set.

...
print("_________by using set()__________")
s=set()
print(s)
print(type(s))

print("\n\n____B.using known elements____\n")
b={"table","fan","fridge"}
print(b)
print(type(b))

print("\n\n_____C.using dynamic data______\n")
v=eval(input("enter set : "))
print(v)
print(type(v))

print("\n_____2.updating______\n")
print("\n_______A.add_______\n")
a={1,2,3,4,5,6,7}
a.add("nandu")
print(a)
print(type(a))

print("___________")

b={1,2,3,4,5,6,7,89,10203}
b.add(("suchi",100))
print(b)
print(type(b))

print("\n_____B.update_______\n")
c={20,40,80,300,400,1234,"bhavya","alakam"}
c.update((1,2,3,4))
print(c)
print(type(c))

print("____________")

d={100,200,300,400,500}
d.update(range(5))
print(d)
print(type(d))

print("________")

s={1,2,3,4,5,6,7,8,9}
r={"bhanu","suchi"}
s.update(r)
print(s)
print(type(s))

print("\n______3.cloning________\n")
s={10,20,30,40,50}
s1=s.copy()
print(s)
print(s1)
print(type(s))

print("\n_______4.deleting_________\n")
print("\n\n_____A.remove_____\n")
f={"ram","rom","processor","harddisk"}
f.remove("processor")
print(f)
print(type(f))

print("\n\n______B.discard______\n")
s={1000,2000,3000,4000}
s.discard(5000)
print(s)
print(type(s))

print("\n\n______C.pop_______\n")
p={'as','bs','bv'}
p.pop()
print(p)
print(type(p))

print("\n\n______D.clear______\n")
s={123,234,345,456,567,678}
s.clear()
print(s)
print(type(s))

print("\n\n__________________________________________PYTHON SET OPERATIONS_________________________________ ______\n")
print("_______union of two sets{symbol:|}______\n")
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print(s1.union(s2))
print(" Or ")
print(s1|s2)

print("\n\n_____intersection of two sets {symbol:&}_____\n")
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.intersection(s2))
print("or")
print(s1&s2)

print("\n\n___update intersection________\n")
s1={11,12,13,14,15}
s2={12,11,23,24,25}
s3={11,23,45,67,89}
s1.intersection_update(s2,s3)
print(s1)

print("\n\n__difference b/w sets___\n")
s1={10,30,40,"bhanu"}
s2={10,30,40,50}
print(s1.difference(s2))
print("or")
print(s1-s2)

print("\n\n_____symmetric difference b/w sets____\n")
s1={1,2,3,4,5}
s2={1,3,5,7,9}
print(s1.symmetric_difference(s2))
print("or")
print(s1^s2)

print("\n\n_________________________SET COMPARISION_____________________________\n")
a={1,3,5,7,9}
b={2,4,6,8,10}
print(a==b)
print(a!=b)
print(b>a)
print(a<b)
print(a>=b)
print(a<=b)

print("\n\n_______A.issubset()____\n")
a={1,2,3}
b={1,2,3}
print(a.issubset(b))
print("__________")
a={1,2,3}
b={1,2,5}
print(a.issubset(b))

print("\n\n_____B.isdisjoint()__________\n")
a={9,8,7}
b={6,5,4}
print(a.isdisjoint(b))
print("__________")
a={9,8,7}
b={9,8,7}
print(a.isdisjoint(b))

print("\n\n_______C.issuperset()_______\n")
a={1,2,3,4,5,6}
b={1,2,3}
print(a.issuperset(b))
c={1,2,3,4}
d={1,6,8,9}
print(c.issuperset(d))




















