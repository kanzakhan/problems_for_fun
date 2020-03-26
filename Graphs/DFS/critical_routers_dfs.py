'''
for each router, remove it from the network and traverse the
remaining connections to see if you can visit all of the 
remaining routers
V = # vertices
E = # edges
O(V(V+E)) = O(V^2 + VE) ~= O(V^2) time, O(E) space 
'''

def check_if_critical_router(adj_list, removed_router):
    visited_routers = set()

    # start search from 0th router when checking if any other router is critical
    # if checking 0th router, start search with Router #1... 
    curr_router = 0 if removed_router != 0 else 1

    # dfs all connections:
    dfs(adj_list, removed_router, curr_router, visited_routers)

    return len(visited_routers)

# all routers that can only be reached via removed_router will NOT be visited during DFS
def dfs(adj_list, removed_router, curr_router, visited_routers):
        # base case
        if curr_router in visited_routers or curr_router == removed_router:
            return
        
        visited_routers.add(curr_router)
        for connected_router in adj_list[curr_router]:
            dfs(adj_list, removed_router, connected_router, visited_routers)

def get_adjacency_list(connections, numRouters):
    adj_list = [[] for _ in range(numRouters)]

    # index in list = the given router
    # value at index is the connections 
    for u, v in connections:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

def critical_routers(numRouters, numConnections, connections):
    # Only 2 routers...
    if numRouters < 3:
        return []

    critical_routers = []

    # establish connections
    adj_list = get_adjacency_list(connections, numRouters)

    for router_index in range(numRouters):
       
        num_routers_checked = check_if_critical_router(adj_list, router_index)
        # subtract 1 from num of routers since one is removed for dfs
        if num_routers_checked < numRouters - 1:
            critical_routers.append(router_index)
    
    return critical_routers