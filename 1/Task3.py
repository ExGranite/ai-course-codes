import numpy as np

f = open('L3.txt', 'r')
position = int(f.readline())
connections = int(f.readline())
graph = np.zeros((position, position), dtype = int)
for e in range(connections):
    line = f.readline().split()
    x = int(line[0])
    y = int(line[1])
    graph[y, x] = 1
lina = int(f.readline())
participant = int(f.readline())
players = []
for i in range(participant):
    players.append(int(f.readline()))

unvisited = [True] * position
moves = [0] * position
queue = []

unvisited[lina] = False
queue.append(lina)
while len(queue) != 0:
    a = queue.pop(0)
    for column in range(position):
        if graph[a][column] == 1:
            if unvisited[column]:
                unvisited[column] = False
                moves[column] = moves[a] + 1
                queue.append(column)

p_moves = []
for i in players:
    p_moves.append(moves[i])

min_moves = min(p_moves)

for i in range(len(p_moves)):
    if min_moves == p_moves[i]:
        print('The participant at position', players[i], 'reaches Lina in shortest', min_moves, 'move(s).')