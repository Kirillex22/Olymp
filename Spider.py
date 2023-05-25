# -*- coding: utf-8 -*- 
a, b, c = map(int, input().split()) 
sx, sy, sz = map(int, input().split()) 
fx, fy, fz = map(int, input().split()) 
s = (sx,sy,sz)
f = (fx,fy,fz)
count = 0
comb = [(a,0,0),(0,b,0),(0,0,c)] 
distance = round(((sx-fx)**2 + (sy-fy)**2 + (sz-fz)**2)**0.5,3)
omg1 = []
omg2 = []
def loc_s(i): 
    global a,b,c
    if (i[0] == a or i[0] == 0) and (i[1] != 0 and i[2] != 0):# плоскость, ортогон Ох 
        if i[0] == a: 
            return a 
        else: 
            return a+1 
    elif (i[1] == b or i[1] == 0) and (i[0] !=0 and i[2] != 0):# плоскость, ортогон Оy 
        if i[1] == b: 
            return b                                                               
        else: 
            return b+1 
     
    elif (i[2] == c or i[2] == 0) and (i[0] !=0 and i[1] != 0):# плоскость, ортогон Оz 
        if i[2] == c: 
            return c 
        else: 
            return c+1

def dof(s,p,M): #точка, направляющий вектор ребра #distance_ortogonal_flats 
     x1 = abs(M[0] - s[0]) 
     y1 = abs(M[1] - s[1]) 
     z1 = abs(M[2] - s[2]) 
     x2 = p[0] 
     y2 = p[1] 
     z2 = p[2]
     d1 = (((x1*z2-x2*z1)**2 + (y2*z1-y1*z2)**2 + (x1*y2-x2*y1)**2)**0.5)/((x2**2 + y2**2 + z2**2)**0.5) 
     return d1

h = loc_s(s)
w = loc_s(f)
print(h,w)

def d_ortoflats():
    global h,w, comb,a,b,c,s,f
    p,m   
    k = []
    if (h==a and w == b) or (h==b and w==a):
        p = comb[2]
        m = (a,b,c/2)
    elif (h == a and w == b+1) or (h == b+1 and w == a):
        p = comb[2]
        m = (a,0,c/2)
    elif (h == a and w == c) or (h == c and w == a):
        p= comb[1]
        m = (a,b/2,c)
    elif (h == a and w == c+1) or (h == c+1 and w == a):
        p = comb[1]
        m = (a,b/2,0)
    elif (h == b and w == c) or (h == c and w == b):
        p = comb[0]
        m =(a/2,b,c)
    elif (h == b and w == c+1) or (h == c+1 and w == b):
        p = comb[0]
        m =(a/2,b,0)
    elif (h == a+1 and w == b) or (h == b and w == a+1):
        p = comb[2]
        m =(0,b,c/2)
    elif (h == a+1 and w == b+1) or (h == b+1 and w == a+1):
        p = comb[2]
        m = (0,0,c/2)
    elif (h == a+1 and w == c) or (h == c and w == a+1):
        p= comb[1]
        m = (0,b/2,c)
    elif (h == a+1 and w == c+1) or (h == c+1 and w == a+1):
        p = comb[1]
        m = (0,b/2,0)
    elif (h == b+1 and w == c) or (h == c and w == b+1):
        p = comb[0]
        m =(a/2,0,c)
    elif (h == b+1 and w == c+1) or (h == c+1 and w == b+1):
        p = comb[0]
        m =(a/2,0,0)
    k = [dof(s,p,m) + (distance**2 - dof(s,p,m)**2)**0.5, dof(f,p,m) + (distance**2 - dof(f,p,m)**2)**0.5]
    print(round(min(k),3))

def coll_flats(omg1, omg2): #omg = [0,1,2,3] 0,1 - 1st class, 2-3 - 2nd class
    global s,f, distance
    this = []
    that = []
    res = [0,0,0,0]
    for i in omg1:
        this.append(dof(s, i[0], i[1]))
    for i in omg2:
        that.append(dof(f, i[0], i[1]))
    for i in range(4):
        res[i] = this[i] + that[i] + (distance**2 - (this[i] - that[i])**2)**0.5
    print(round(min(res),3))
    

if (h == w):
    print(distance) #одинаковые
else:
    if (h == a and w == a + 1) or (h == a+1 and w == a): #параллельные/смежные
        if h == a and w == a + 1:
            omg1 = [(comb[1], (a,b/2,c)), (comb[1], (a,b/2,0)), (comb[2], (a,0,c/2)), (comb[2], (a,b,c/2))] #a to a+1
            omg2 = [(comb[1], (0,b/2,c)), (comb[1], (0,b/2,0)), (comb[2], (0,0,c/2)), (comb[2], (0,b,c/2))]
        else:
            omg2 = [(comb[1], (a,b/2,c)), (comb[1], (a,b/2,0)), (comb[2], (a,0,c/2)), (comb[2], (a,b,c/2))] #a+1 to a
            omg1 = [(comb[1], (0,b/2,c)), (comb[1], (0,b/2,0)), (comb[2], (0,0,c/2)), (comb[2], (0,b,c/2))]

    elif (h == b and w == b+1) or (h == b+1 and w == b):
        if h == b and w == b+1:
            omg1 = [(comb[2], (0,b,c/2)), (comb[2], (a,b,c/2)), (comb[0], (a/2,b,0)), (comb[0], (a/2,b,c))] #b to b+1
            omg2 = [(comb[2], (0,0,c/2)), (comb[2], (a,0,c/2)), (comb[0], (a/2,0,0)), (comb[0], (a/2,0,c))] 
        else:
            omg2 = [(comb[2], (0,b,c/2)), (comb[2], (a,b,c/2)), (comb[0], (a/2,b,0)), (comb[0], (a/2,b,c))] #b+1 to b
            omg1 = [(comb[2], (0,0,c/2)), (comb[2], (a,0,c/2)), (comb[0], (a/2,0,0)), (comb[0], (a/2,0,c))]

    elif (h == c and w == c+1) or (h == c+1 and w == c):
        if h == c and w == c+1:
            omg1 = [(comb[0], (a/2,0,c)), (comb[0], (a/2,b,c)), (comb[1], (0,b/2,c)), (comb[1], (a,b/2,c))] #c to c+1
            omg2 = [(comb[0], (a/2,0,0)), (comb[0], (a/2,b,0)), (comb[1], (0,b/2,0)), (comb[1], (a,b/2,0))]
        else:
            omg2 = [(comb[0], (a/2,0,c)), (comb[0], (a/2,b,c)), (comb[1], (0,b/2,c)), (comb[1], (a,b/2,c))] #c+1 to c
            omg1 = [(comb[0], (a/2,0,0)), (comb[0], (a/2,b,0)), (comb[1], (0,b/2,0)), (comb[1], (a,b/2,0))]
    else:
        d_ortoflats()
        count = 1
    if count == 0:
        coll_flats(omg1, omg2)
    







 
    





















 
 
 


