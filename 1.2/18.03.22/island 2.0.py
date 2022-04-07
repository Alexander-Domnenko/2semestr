import numpy as np
filename=input('Введите полное имя файла: ')
with open(filename, 'r') as file:
    mas = file.readlines()
mas = [[int(n)for n in x.split()] for x in mas]
mas2=np.array(mas)
mas=np.pad(mas2,((1,1)),'constant')
output=[]
for num in range(1,9+1):
    def mark(mas,i,j):
        mas[i][j]=0;
        
        if mas[i][j-1] ==num:
            mark(mas,i,j-1)
       
        if mas[i][j+1]==num:
            mark(mas,i,j+1)
      
        if mas[i-1][j]==num:
            mark(mas,i-1,j)
     
        if mas[i+1][j]==num:
            mark(mas,i+1,j)
    k=0  
    g=0
    count=0
    for i in range(0, len(mas)):
        for j in range(0, len(mas[i])):
            if mas[i][j] ==num:
                mark(mas,i,j)
                count+=1 
    k+=count
    g=g+k
    output.append(g)
    print('острова из',num, '=',g)
print(sum(output))
