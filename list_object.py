print("______________________________________1.LIST OBJECT_____________________________________________")
print("\n\n____________1.creating_____________\n\n")
print("_____A.creating empty list_____\n")
l=[]
print(l)
print(type(l))

print("\n\n____B.creating list objectby using some known elements_____\n")
l=[20,5,'bhavya',"suchi",'bhanu',142,"1234"]
print(l)
print(type(l))

print("\n\n____C.creating list object with dynamic data______\n")
l=eval(input("enter list : "))
print(l)
print(type(l))

print("\n\n____D.by using split______\n")
data="banana apple orange mango"
b=data.split(" ",2)
print(b)
print(type(b))
print("____")
d="1 2 3 b s v"
b=d.split(" ",3)
print(b)
print(type(b))

print("\n\n___E.creating list obj using list[]___\n")
b="123"
v="bhavya"
s='suchi'
l1=list(b)
print(l1)
print(type(l1))
l2=list(v)
print(l2)
print(type(l2))
l3=list(s)
print(l3)
print(type(l3))

print("\n\n_______________2.retrieving_____________\n")
print("___________A.indexing___________\n")
i=["bhavya",1,2,3,'suchi']
print(i[4])
print(type(i))

print("___________")

r=["home",300,96,'chocolate']
print(r[3])
print(type(r))

print("\n\n_________B.slicing/accessing_____________\n")
b=['suchi',"likes",'bhanu']
print(b[-1][::-1])
print(type(b))

print("_______________")

v=['12345','cherry','banana','apple']
print(v[::-1])
print(type(v))

print("_______________")

s=["suchi",'nandu',"bhavi",'chaithu',"varu"]
print(s[-3][-2:-6:-3])
print(type(s))

print("\n\n_______C.count_________\n")
c=[1,2,3,4,1,2,4,5,6,7,98,"bhavya",'sanju',"bhavya",1,2,3]
print(c.count("bhavya"))
print(type(c))

print("_____________________")

d=[0,1,2,3,4,5,4,3,2,1,1,2,3,4,2,1,1,1,1]
print(d.count(1))
print(type(d))

print("\n\n___________3.updating___________\n")

print("__________A.append_________\n")
e=[1,2,3,10,20,'book']
e.append(1000)
print(e)
print(type(e))

print("_______________")

e=[1,2,3,10,20,'book']
e.append([1,1000])
print(e)
print(type(e))

print("\n\n________B.extend________\n")
f=['suchi','bhaskar','nandu',"sanju"]
f.extend(["bhanu",'varu',123])
print(f)
print(type(f))

print("______________")

g=['bhanu','suchi']
g.extend(range(10))
print(g)
print(type(g))

print("_________________")

h=[1,2,3,4,5]
j=[6,7,8,9,10]
h.extend(j)
print(h)
print(type(h))

print("\n\n_________C.inserting_________\n")
k=[1,2,3,4,"alakam","sree"]
k.insert(5,"bhavya")
print(k)
print(type(k))

print("\n\n_________D.reverse_________\n")
m=[1,2,9,'bhanu','sree']
m.reverse()
print(m)
print(type(m))

print("\n\n_______E.sort__________\n")
n=[1,4,5,3,10,20,0]
n.sort()
print(n)
n.sort(reverse=True)
print(n)
print(type(n))

print("\n\n_________F.concatination___________\n")
l1=[10,20,30]
l2=[40,50,60]
l3=l1+l2
print(l3)
print(type(l3))

print("\n\n_______H.reretition______________\n")
v1=[1,2,3]
v2=v1*2
print(v2)
print(type(v2))

print("__________________")
l1=["bhanu",'suchi',"nandu"]
l2=l1*3
print(l2)
print(type(l2))

print("\n\n_______4.deleting____________\n")
print("_______A.remove______\n")
o=[1,2,'bhanu',"bag",90]
o.remove(2)
print(o)
print(type(o))

print("\n\n_______B.pop______\n")
p=[3,4,7,"mobile","tab"]
p.pop()
print(p)
print(type(p))

print("\n\n________C.clear________\n")
q=[1,2,3,5,7,9]
q.clear()
print(q)
print(type(q))









