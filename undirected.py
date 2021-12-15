from sys import stdin

def adjacency_list():
    nodes = int(input())
    adjacency = [set([]) for _ in range(nodes)]
    for line in stdin:
        nodes = line.split(" ")
        first = int(nodes[0])
        second = int(nodes[1])
        adjacency[first].add(second)
        adjacency[second].add(first)
    return adjacency

def find_connected_component(adjacency, visited):
    i = 0
    while(i<len(visited) and visited[i] == True):
        i+=1
    if(i==len(visited)):
        return False
    q = [i]
    visited[i] = True
    while(q != []):
        cur = q.pop(0)
        for neighbor in adjacency[cur]:
            if(visited[neighbor]):
                continue
            else:
                q.append(neighbor)
                visited[neighbor] = True
    return True

def count_connected_components(adjacency, visited):
    connected_components = 0
    while(find_connected_component(adjacency, visited)):
        connected_components += 1
    return connected_components

if __name__ == '__main__':
    adjacency = adjacency_list()
    visited = [False for _ in range(len(adjacency))]
    print(count_connected_components(adjacency, visited))
