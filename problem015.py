# -*- coding: utf-8 -*-

LENGTH = 20

maze = []
for i in range(LENGTH + 1):
    maze.append([0 for j in range(LENGTH + 1)])

maze[0][0] = 1
for i in range(LENGTH + 1):
    for j in range(LENGTH + 1):
        if i != 0:
            maze[i][j] += maze[i-1][j]
        if j != 0:
            maze[i][j] += maze[i][j-1]

print(maze[LENGTH][LENGTH])