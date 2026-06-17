print("______________________TUPLE DATA STRUCTURE______________________________")
print("\n_________________1.creating__________________\n")
print("____A.creating empty tuple_____\n")
a=()
print(a)
print(type(a))

print("\n\n____B.creating tuple object by using some known elements____\n")
b=(1,2,'bhanu',"book")
print(b)
print(type(b))

print("________________")
f=1,2,"book"
print(f)
print(type(f))


print("\n\n____c.creating tuple object with dynamic data____\n")
c=eval(input("enter tuple : "))
print(c)
print(type(c))

print("\n\n____D.creating list obj using tuple()_________\n")
d=b="bhavya"
v="varu"
t1=tuple(b)
print(t1)
print(type(t1))
t2=tuple(v)
print(t2)
print(type(t2))

print("\n_________2.accessing/retreiving_________\n")
print("_____A.indexing_________\n")
v=("bhaskar",1234,"sanju")
print(v[-1])
print(type(v))

print("___________")

t3=100,200,300,100,200,300,400,600,10000,999,"bhanu"
print(t3.index(100))
print(type(t3))
print(t3.index("bhanu"))

print("\n\n___B.slicing_____\n")
s=("nandu","123456",'tab')
print(s[1][-1:-7:-1])
print(type(s))

print("\n\n____C.count______\n")
n=(1,2,3,'bhanu',100,299,'bhanu')
print(n.count('bhanu'))
print(type(n))

print("____________")
t=10,20,1,2,3,4,5,6,7,8,9
print(len(t))

print("\n\n_____D.concatination_____\n")
m=("alakam","bhavya")
o=("bhaskar","naidu")
p=m+o
print(p)
print(type(p))

print("\n\n_____E.repetition_____\n")
r=10,20,30
print(r*2)
print(type(r))

print("_____")
s=(10,20,30,40,50)
print(s*2)
print(type(s))

print("\n\n_____F.sorted____\n")
s=('alakam','bhanu',"suchi","bhavya")
s1=sorted(s)
print(s1)
print(type(s1))

print("\n\n________G.maximum value________\n")
z=10,20,90,14234,1000000,1234567890
print(max(z))
print(type(z))

print("\n\n________H.manimum value_______\n")
y=-1,0,23,6754,0b1010101,-1234,1234
print(min(y))
print(type(y))

print("\n\n_______I.comparing varaibles__________\n")
a=10,20
b=20,30
c=30,40,50
d=a,b,c
print(d)
print(type(d))

print("\n\n_____J.tuple comprehension_____\n")#tuple comprehension is not possible
t=(2*x for x in range(10))
print(t)
print(type(t))


















