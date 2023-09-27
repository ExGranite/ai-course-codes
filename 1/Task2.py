import numpy as np

f = open('L2.txt', 'r')
position = int(f.readline())
connections = int(f.readline())
graph = np.zeros((position, position), dtype = int)
for e in range(connections):
    line = f.readline().split()
    x = int(line[0])
    y = int(line[1])
    graph[x, y] = 1
    graph[y, x] = 1
lina = int(f.readline())
nora = int(f.readline())
lara = int(f.readline())

unvisited = [True] * position
moves = [0] * position
queue = []

unvisited[nora] = False
queue.append(nora)
while len(queue) != 0:
    a = queue.pop(0)
    for column in range(position):
        if graph[a][column] == 1:
            if unvisited[column]:
                unvisited[column] = False
                moves[column] = moves[a] + 1
                queue.append(column)
for_nora = moves[lina]

unvisited = [True] * position
moves = [0] * position
queue = []

unvisited[lara] = False
queue.append(lara)
while len(queue) != 0:
    a = queue.pop(0)
    for column in range(position):
        if graph[a][column] == 1:
            if unvisited[column]:
                unvisited[column] = False
                moves[column] = moves[a] + 1
                queue.append(column)
for_lara = moves[lina]

if for_nora < for_lara:
    print('Nora reaches Lina first.')
elif for_nora > for_lara:
    print('Lara reaches Lina first.')
else:
    print('Nora and Lara both reach Lina at the same time.')