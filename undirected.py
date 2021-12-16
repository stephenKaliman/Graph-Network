from sys import stdin

def adjacency_list(graph_file):
    graph = open(graph_file, "r")
    nodes = int(graph.readline())
    adjacency = [set([]) for _ in range(nodes)]
    for line in graph:
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

def read_and_count(graph_file):
    adjacency = adjacency_list(graph_file)
    visited = [False for _ in range(len(adjacency))]
    return count_connected_components(adjacency, visited)

if __name__ == '__main__':
    print("n10:\t"+str(read_and_count("./graphs/n10.txt")))
    print("n100:\t"+str(read_and_count("./graphs/n100.txt")))
    print("n1000:\t"+str(read_and_count("./graphs/n1000.txt")))
    print("n10000:\t"+str(read_and_count("./graphs/n10000.txt")))
    print("s1:\t"+str(read_and_count("./graphs/s1.txt")))
