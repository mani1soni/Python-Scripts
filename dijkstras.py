g = {
    'A' : [('B',10), ('C',10)],
    'B' : [('D',1)],
    'C' : [('F',5)],
    'D' : [('E',5), ('F',3)],
    'E' : [('G',5)],
    'F' : [('G',5)],
    'G' : []
}


## This is custom implementation of Priority Queue. You can also use inbuilt python functionality of priority queues
def find_min_node(d, visited):
    min_node = None
    min_value = float("inf")
    for k, v in d.iteritems():

        if min_value > v[0] and k not in visited:
            min_value = v[0]
            min_node = k

    return min_node


def dijkstras(g, s, e):
    keys = g.keys()
    visited = []
    min_dist = {}  # 'A' : (0,A), 'B' : (10,A)
    min_dist[s] = (0, s)

    while len(keys) != len(visited):
        min_node = find_min_node(min_dist, visited)

        if not min_node:
            break
        neighbors = g[min_node]
        visited.append(min_node)

        for neigh in neighbors:
            if neigh[0] in min_dist:
                if min_dist[min_node][0] + neigh[1] < min_dist[neigh[0]][0]:
                    min_dist[neigh[0]] = (min_dist[min_node][0] + neigh[1], min_node)
            else:
                min_dist[neigh[0]] = (min_dist[min_node][0] + neigh[1], min_node)

    path = []
    current = e
    path.append(current)
    while current != s:
        path.append(min_dist[current][1])
        current = min_dist[current][1]

    return min_dist, path[::-1]

shortest_path = dijkstras(g,'A','G')
print (shortest_path) # A, B, D, F, G