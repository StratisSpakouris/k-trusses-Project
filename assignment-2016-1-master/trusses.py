import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of input file")
parser.add_argument("k_nodes", help="number of vertices", 
                    type=int, default=2)

args = parser.parse_args()

f = open(args.filename)
pairs = f.read()

def size_of_intersection(a,b):
    count = 0
    for i in a:
        for j in b:
            if i==j:
                count+=1
    return count

def is_duplicate(a,b):
    if (len(a) != len(b)):
        return False
    is_d = True
    for i in a:
        exists = False
        for j in b:
            if i == j:
                exists = True
        if exists == False:
            is_d = False
            return is_d
    return is_d
            

x = [int(i) for i in pairs.split()]
graph = {}
for i in x:
    neighbours = []
    graph [i] = neighbours
for i in range(0, len(x), 2):
    graph[x[i]].append(x[i+1])
    graph[x[i+1]].append(x[i])
## print (graph)

change = True
while (change == True):
    change = False
    for i in range (0, len(x), 2):
        if(x[i]!=-1):
            if (size_of_intersection(graph[x[i]], graph[x[i+1]]) < args.k_nodes-2):
                graph[x[i]].remove(x[i+1])
                graph[x[i+1]].remove(x[i])
                x[i]=-1
                x[i+1]=-1
                change = True

k_trusses = []

for i in graph:
    truss = []
    if (len(graph[i]) > 0):
        truss.append(i)
        for j in graph[i]:
            truss.append(j)
    insert_truss = True
    for t in k_trusses:
        if is_duplicate(truss, t):
            insert_truss = False
    if insert_truss == True:
        k_trusses.append(truss)


for k in k_trusses:
    k.sort()
k_trusses.sort()        
          
for k in k_trusses:
    if (len(k) > 0):
        k.sort()
        t = tuple(k)
        print (t)  