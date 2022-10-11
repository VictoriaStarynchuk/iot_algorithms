from lab2.bfs import ShortestSafestPath

if __name__ == "__main__":
    matrix = ShortestSafestPath("input.txt")
    path = matrix.bfs
    f = open("output.txt", "w")
    f.write(str(path))
