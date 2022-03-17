filename=input('Введите полное имя файла: ')
with open(filename, 'r') as file:
    mas = file.readlines()
mas = [[int(n)for n in x.split()] for x in mas]
def mark(mas,i,j):
    mas[i][j]=0;
    if mas[j-1] in mas:
        if mas[i][j-1] ==1:
            mark(mas,i,j-1)
    if mas[j+1] in mas:
        if mas[i][j+1]==1:
            mark(mas,i,j+1)
    if mas[i-1] in mas:
        if mas[i-1][j]==1:
            mark(mas,i-1,j)
    if mas[i+1] in mas:
        if mas[i+1][j]==1:
            mark(mas,i+1,j)
count=0
for i in range(0, len(mas)):
    for j in range(0, len(mas[i])):
        if mas[i][j] ==1:
            mark(mas,i,j)
            count+=1
print(count)
