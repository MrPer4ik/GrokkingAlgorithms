from collections import deque

def bfs(graph, start, finish):
    if start == finish:
        return True
    else:
        deq = deque()
        deq.extend(graph[start])
        checked = []
        while len(deq) > 0:
            curr = deq.popleft()
            if curr not in checked:
                if curr == finish:
                    return True
                else:
                    checked.append(curr)
                    deq.extend(graph[curr])
            print(checked)
        return False

graph = {}
graph ["you"] = [ "alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(bfs(graph, 'you', 'thom'))
print(graph)