import numpy as np

f = open('L1.txt', 'r')
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

unvisited = [True] * position
moves = [0] * position
queue = []

unvisited[0] = False
queue.append(0)
while len(queue) != 0:
    a = queue.pop(0)
    for column in range(position):
        if graph[a][column] == 1:
            if unvisited[column]:
                unvisited[column] = False
                moves[column] = moves[a] + 1
                queue.append(column)
print('The minimum number of move(s) for Nora to reach Lina is/are', moves[lina], end = '.\n')