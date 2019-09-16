def find_min(paths, checked):
    min = float('inf')
    min_item = None
    for item in paths.keys():
        if paths[item] < min and item not in checked:
            min = paths[item]
            min_item = item
    return min_item
        

def dejkstra(graph, paths, parents, checked):
    while len(checked) < len(graph):
        curr = find_min(paths, checked)
        curr_path = paths[curr]
        for child in graph[curr].keys():
            if graph[curr][child] + curr_path < paths[child]:
                paths[child] = graph[curr][child] + curr_path
                parents[child] = curr
        checked.append(curr)

def find_path(parents):
    curr = 'End'
    result = [curr]
    while parents[curr]:
        result.append(parents[curr])
        curr = parents[curr]
    return result

graph = {}
graph['Start'] = {'B': 5, 'C': 2}
graph['B'] = {'D': 4, 'E': 2}
graph['C'] = {'B': 8, 'E': 7}
graph['D'] = {'E': 6, 'End': 3}
graph['E'] = {'End': 1}
graph['End'] = {}

paths = {}
parents = {}
for key in graph.keys():
    if key is not 'Start':
        paths[key] = float('inf')
    else:
        paths[key] = 0
    parents[key] = None

checked = []

dejkstra(graph, paths, parents, checked)
print(paths)
path = find_path(parents)[::-1]
for node in path:
    print(node + ' -> ' if node is not 'End' else node, end='')