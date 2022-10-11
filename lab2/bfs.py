from collections import deque

from lab2.node import Node, row, is_valid, col


class ShortestSafestPath:
    def __init__(self, file_with_matrix):
        with open(file_with_matrix, 'r') as file:
            graph = [[int(num) for num in line.split(' ')] for line in file]
        self.graph = graph
        self.height = len(self.graph)
        self.width = len(self.graph[0])

    @property
    def bfs(self):
        obstacle = 7
        for x in range(self.height):
            for y in range(self.width):
                if self.graph[x][y] == 0:
                    for i in range(len(row)):
                        if is_valid(x + row[i], y + col[i], self.width, self.height):
                            self.graph[x + row[i]][y + col[i]] = obstacle

        is_visited = [[False for x in range(self.width)] for y in range(self.height)]

        queue = deque()

        for x in range(self.height):
            if self.graph[x][0] == 1:
                queue.append(Node(x, 0, 0))
                is_visited[x][0] = True

        while queue:
            curr_node = queue.popleft()
            x = curr_node.get_x()
            y = curr_node.get_y()
            distance = curr_node.get_dist()

            for i in range(len(row)):
                if is_valid(x + row[i], y + col[i], self.width, self.height) and self.graph[x + row[i]][y + col[i]] == 1:
                    is_visited[x + row[i]][y + col[i]] = True
                    queue.append(Node(x + row[i], y + col[i], distance + 1))
            if y == self.width - 1:
                return distance