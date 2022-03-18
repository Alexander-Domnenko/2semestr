c=0
a=input().split()
b= list(map(int, a))
for i in b:
    if i%2==0:
        c+=1
print(c)
