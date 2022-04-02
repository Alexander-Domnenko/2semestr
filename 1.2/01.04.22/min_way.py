print('код не работает')
mass = [
        [0,5,3,15],
        [99,0,10,99],
        [99,99,0,6],
        [99,99,99,0]
        ]

l = len(mass)                       
for k in range(l):
    for i in range(l):
        for j in range(l):
            if mass[i][k]+mass[k][j]<mass[i][j]:
                mass[i][j]=mass[i][k]+mass[k][j]
                r=mass[i][j]
                
print(r)




        
