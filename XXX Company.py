g = []
res = []
s = []
while True:
    x = str(input())
    if x == "END":
        break
    y = str(input())
    if (len(y) < 5):
        y += " Unknown Name"
    t = (x,y)
    g.append(t) #(XXXX_NAME нач, XXXX_NAME)
name = input().lower()
k = 1
try:
    int(name)
except:
    k = 0
if name == "Unknown Name":
    print("index")
    name = str(input())
    k = 1
for i in g:
   if k == 1:
       if i[0][0:4] == name:
           res.append(i[1])
   elif k == 0:
       if i[0][5:len(i[0])].lower() == name:
           res.append(i[1])
if len(res) == 0:
    print("NO")
else:
    for i in res:
        s.append(int(i[0:4]))
    s.sort()
    for i in s:
        for j in res:
            if i == int(j[0:4]):
                print(j)
