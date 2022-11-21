from collections import *
import math

class Node:
    def __init__(self, id, name, dur, es, ef, ls, lf) -> None:
        self.id = id
        self.name = name
        self.dur = dur
        self.es = es
        self.ef = ef
        self.ls = ls
        self.lf = lf

forwardPass = defaultdict(list)
backwardPass = defaultdict(list)
q = deque()
seq = deque()
criticalPath = []
totalDuration = 0
nodes = {}
visited = {}
leafs = {}

file = open("././input.txt")

for lines in file:
    line = lines.rstrip('\n').split(',')
    id, name, dur = int(line[0]), line[1], int(line[2])
    ef = 0
    if(len(line) == 4):
        predecessors = line[3].split(';')
        for x in predecessors:
            x = int(x)
            forwardPass[x].append(id)
            backwardPass[id].append(x)
    else:
        ef = dur
        q.append(id)
    
    nodes[id] = Node(id,name,dur, 0, ef, 0, math.inf)
    visited[id] = 0
    leafs[id] = 0

while q:
    u = q.popleft()
    ef = nodes[u].ef
    outDegree = 0
    for v in forwardPass[u]:
        nodes[v].es = max(ef, nodes[v].es)
        nodes[v].ef = nodes[v].es + nodes[v].dur

        if(visited[v] != 1):
            q.append(v)
            outDegree +=1


    if(outDegree == 0 and visited[u] == 0):
        leafs[u] = 1
        totalDuration = max(totalDuration, nodes[u].ef)

    visited[u] = 1

for node, leaf in leafs.items():
    if(leaf == 1):
        nodes[node].lf = totalDuration
        nodes[node].ls = nodes[node].lf - nodes[node].dur

        q.append(node)
        seq.append(node)

    visited[node] = 0


while q:
    u = q.popleft()
    ls = nodes[u].ls
    for v in backwardPass[u]:
        nodes[v].lf = min(ls, nodes[v].lf)
        nodes[v].ls = nodes[v].lf - nodes[v].dur

        if(visited[v] != 1):
            q.append(v)

    visited[u] = 1

while seq:
    u = seq.popleft()
    
    if(nodes[u].lf == nodes[u].ef):
        criticalPath.append(nodes[u].name)
        
        for v in backwardPass[u]:
            v = int(v)
            if(visited[v] != 0):
                seq.append(v)

    visited[u] = 0

for i in nodes:
    print(f'id = {nodes[i].id},node = {nodes[i].name},duration = {nodes[i].dur},ES = {nodes[i].es},\
    EF = {nodes[i].ef},LS = {nodes[i].ls},LF = {nodes[i].lf}')

criticalPath.reverse()
print(criticalPath)
