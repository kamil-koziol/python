# ZASADA DZIAŁANIA
# G-COST - Distance from starting node
# H-COST - Distance from end node
# F-COST - G+H
# NA UKOS 2
# NA BOKI 1
class Node:
    def __init__(self, pos, g, h, av):
        self.grid_pos = pos
        self.g_cost = g
        self.h_cost = h
        self.f_cost = self.g_cost + self.h_cost

class Grid:
    def __init__(self, x_size, y_size):
        self.size = (x_size, y_size)
    
    def __len__(self):
        return self.size[0] * self.size[1]

def get_dist(a,b):
    return (b[0]-a[0])**2 + (b[1]-a[1])**2

def get_maze():
    """ Zwraca listę x na y """
    maze = []
    
    maze.append([" ", " ", " ", " ", " "])
    maze.append([" ", " ", " ", " ", " "])
    maze.append([" ", " ", " ", " ", " "])
    maze.append([" ", " ", " ", " ", " "])
    maze.append([" ", " ", " ", " ", " "])

    return maze

def show_maze(maze):
    for row in maze:
        print(row)

def set_parents(node):
    parents = [
        get_parent(node, 1,0),
        get_parent(node, -1,0),
        get_parent(node, 0,1),
        get_parent(node, 0,-1),
        get_parent(node, 1,1),
        get_parent(node, -1,-1),
        get_parent(node, 1,-1),
        get_parent(node, -1,1),
        ]
    
    for parent in parents:
        if maze[parent[1]][parent[0]] == "X":
            continue
        if maze[parent[1]][parent[0]] == "D":
            return True
        maze[parent[1]][parent[0]] = str(parent[2])
    return False
    

def get_parent(node, x,y):
    dist_from_start = get_dist(start_pos, (node[0]+x, node[1]+y))
    dist_from_end = get_dist(end_pos, (node[0]+x, node[1]+y))
    # maze[node[1]+y][node[0]+x] = str(dist_from_start + dist_from_end)
    return (node[0]+x,node[1]+y,dist_from_start + dist_from_end)

def find_lowest():
    "zwraca x,y najmniejszego"
    lowest = 1000
    lowest_x, lowest_y = 0,0
    for i,y in enumerate(maze):
        for j,x in enumerate(y):
            try:
                x = int(x)
                if x < lowest:
                    lowest = x
                    lowest_x = j
                    lowest_y = i
            except:
                continue
    # maze[lowest_x][lowest_y] = str(x) + "U"
    return lowest_x,lowest_y
            
maze = get_maze(10,10)

start_pos = (8,3)
end_pos = (2,5)

maze[start_pos[1]][start_pos[0]] = "X"
maze[end_pos[1]][end_pos[0]] = "D"

points = []
while not set_parents(start_pos):
    # print()
    # show_maze(maze)
    start_pos = find_lowest()
    points.append(start_pos)


for point in points:
    maze[point[1]][point[0]] = "*"

for row in maze:
    for item in row:
        if item in ("X", "D", "*"):
            print(item, end=" ")
        else:
            print("-", end=" ")
    print()