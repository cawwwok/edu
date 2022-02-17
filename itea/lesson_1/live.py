#int - целое , float - число плавающей .
a = 1
b = 1.0

#print
print(a, type(a))
print(b, type(b))

#bool - истина/ложь
c = True
d = False
print(c, type(c))
print(d, type(d))

#str - строка
e = "helloworld"
e_1 = "net.ua"
print(e,e_1)

#list
l0 = list() or [] #0
l1 = (1, 2, 3, "test string", ValueError) #кортеж с произв.

t0 = tuple () or () # empty

#множество
s0 = set () #empty
s1 = {1,2,3, "test string", ValueError}

#dict
d0 = dict() or {} #empty dict
d1 = {1: "One", 2: "two", 3:"three"} #dict
print (type(d1))
l = [1, 2, 3, 4]
t = (1, 2, 3, 4)
s = {1, 2, 3, 4}
d = {1:"orang",
     2:"apple",
     3:"pineapple"}

#print (d[0])

l.append(123123)
print(l)
s.add(1123123123)
print (s)


#if
h = 10
if h > 1:
    print("lololo h")
elif h == 1:
    print ("dodod h")
else:
    print("dsdsd h")

#while
cnt = 0

while cnt <10:
    print("cnt is", cnt)
    cnt = cnt + 1