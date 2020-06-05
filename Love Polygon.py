import sys
sys.setrecursionlimit(10**6)
def depth(marked, gph, node):
        if node not in marked:
            marked.add(node)
            f_circ.remove(node)
            for neigh in gph[node]:
                depth(marked, gph, neigh)
for _ in range(int(input())):
    gph={}
    marked=set()
    friends=int(input())
    pairs=int(input())
    for init in range(friends):
        gph[init]=[]
    size=[]
    f_circ=list(range(friends))
    for i in range(pairs):
        key,value=map(int,input().split())
        gph[key].append(value)
        gph[value].append(key)
    while len(f_circ)>0:
        curr=f_circ[0]
        depth(marked,gph,curr)
        size.append(len(marked))
        marked.clear()
    print(len(size))
    size=list(map(str,size))
    size.sort()
    print(" ".join(size))
