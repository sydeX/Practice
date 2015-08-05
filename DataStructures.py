graph1 = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

graph2 = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D', 'F'],
             'D': ['C'],
             'F': ['C', 'E']}

def find_shortest_path(g, start, end, path=[]):
    # if not g.get(start):
    #     return None

    path = path + [start]

    if start == end:
        return path

    shortest = None

    for node in g[start]:
        if node not in path:
            newPath = find_shortest_path(g, node, end, path)
            if not shortest or (newPath and len(newPath) < len(shortest)):
                shortest = newPath

    return shortest

def bfs(g, a):
    if not a:
        return []

    queue = [a]
    res = []

    while queue:
        node = queue.pop(0)
        if node not in res:
            res.append(node)
            if g.has_key(node):
                queue.extend(g[node])

    return res

def dfs(g, a):
    if not a:
        return []

    stack = [a]
    res = []

    while stack:
        node = stack.pop(-1)
        if node not in res:
            res.append(node)
            if g.has_key(node):
                stack.extend(g[node])

    return res

def isUniqueString(s):
    if not s:
        return True

    checker = 0

    for i in s:
        offset = ord(i) - ord('a')
        if checker & (1 << offset) == 0:
            checker |= (1 << offset)
        else:
            return False

    return True

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def main():
    print find_shortest_path(graph2, 'A', 'E')
    # print bfs(graph2, 'A')
    # print dfs(graph2, 'A')


    # print isUniqueString(None)
    #
    # d = { 'a':1, 'b':2}

    # a = Node('nancy')
    # b = Node('bob')
    # a.next = b

    # print a.next.data

if __name__ == '__main__':
    main()