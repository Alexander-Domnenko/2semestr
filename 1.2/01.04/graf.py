import math as m
print(' Загрузил, чтобы не потерять код')
ms={i[0]:list(map(int,i.split()[1:])) for i in open('msm.txt').readlines()[1:]}
#ms = {i[0]: i.split()[1:] for i in open('msm.txt').readlines()}


#ms={'A': [0, 13, 8, 5, 7, 17, 13, 16], 'B': [25, 0, 21, 17, 6, 17, 3, 24], 'C': [19, 3, 0, 10, 15, 2, 15, 21], 'D': [10, 9, 18, 0, 20, 0, 12, 20], 'E': [14, 10, 0, 12, 0, 9, 18, 6], 'F': [12, 23, 21, 2, 10, 0, 20, 13], 'G': [4, 4, 9, 10, 22, 12, 0, 13], 'H': [11, 10, 19, 12, 21, 20, 1, 0]}
#print(ms)
l = [print(i, " ".join(map(str, (ms[i])))) for i in ms]



#last=sorted(ms.values())[2]
#last=list(map(int,last))#print(last)
#ms.update(H=last)
#print(ms)
#ms.pop('#')

#print(ms)


inp_correct = False
while not inp_correct:
    src = input('Which startpoint?' + str([i for i in ms.keys()]) + ': ')
    dest = input('Which destpoint?' + str([i for i in ms.keys()]) + ': ')
    inp_correct = src in ms.keys() and dest in ms.keys()
    if not inp_correct:
        print('This is out of graph!')

lengths, paths = {}, {}
visited = []
for i in ms.keys():
    lengths[i] = m.inf
paths[src] = []
lengths[src] = 0 

while dest not in visited:
    #print(dest)
    l = m.inf
    minnode = ''
    for n in filter(lambda x: x not in visited, ms.keys()):
        if l > lengths[n]:
            minnode = n
            l = lengths[n]
            #print(l)
    #for j in range(len(ms[minnode])-1):
        #ms[minnode]=list(map(int,ms[minnode]))
        #print(ms[minnode])
    visited.append(minnode)
   # print(ms[minnode])
    for i in range(len(ms[minnode])):
        print(ms[minnode][i])
        if ms[minnode][i] == 0:
            continue
        curnode = list(ms.keys())[i]
    
        #print (lengths[minnode])
        
        if ms[minnode][i] + lengths[minnode] < lengths[curnode]:
            
            lengths[curnode] = ms[minnode][i] + lengths[minnode]
            paths[curnode] = paths[minnode] + [minnode]

#print(ms)
way="".join(paths[dest]+[dest])
#print(way)


#print(paths)
#print(lengths)
