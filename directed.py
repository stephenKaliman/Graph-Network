from sys import stdin

def adjacency_lists():
    nodes = int(input())
    fwd_adjacency = [set([]) for _ in range(nodes)]
    rev_adjacency = [set([]) for _ in range(nodes)]
    for line in stdin:
        nodes = line.split(" ")
        first = int(nodes[0])
        second = int(nodes[1])
        fwd_adjacency[first].add(second)
        rev_adjacency[second].add(first)
    return (fwd_adjacency, rev_adjacency)

def find_weakly_connected_component(single_dir_adjacency, visited, root):
    # local copy of visited
    tmp_vis = [x for x in visited]
    # keep set of nodes reachable in set
    reachable = set([])
    # begin BFS
    q = [root]
    tmp_vis[root] = True
    while(q != []):
        cur = q.pop(0)
        # as popped, add to reachable set
        reachable.add(cur)
        for neighbor in single_dir_adjacency[cur]:
            if(tmp_vis[neighbor]):
                continue
            else:
                q.append(neighbor)
                tmp_vis[neighbor] = True
    return reachable

def find_strongly_connected_component(fwd_adjacency, rev_adjacency, visited):
    i = 0
    while( i < len(visited) and visited[i] == True):
        i += 1
    if ( i == len(visited) ):
        return False
    
    fwd_connected = find_weakly_connected_component(fwd_adjacency, visited, i)
    rev_connected = find_weakly_connected_component(rev_adjacency, visited, i)
    strongly_connected = fwd_connected.intersection(rev_connected)

    for node in strongly_connected:
        visited[node] = True

    return True

def count_strongly_connected_components(fwd_adjacency, rev_adjacency, visited):
    strongly_connected_components = 0
    while(find_strongly_connected_component(fwd_adjacency, rev_adjacency, visited)):
        strongly_connected_components += 1
    return strongly_connected_components

if __name__ == '__main__':
    fwd_adjacency, rev_adjacency = adjacency_lists()
    visited = [False for _ in range(len(fwd_adjacency))]
    print(count_strongly_connected_components(fwd_adjacency, rev_adjacency, visited))
