from graphs import graph

graph_elements = { 
   #node:  (heuristice, {neighbours:cost})
   "s" : (24, {"a":3, "b":9,"c":4}),
   "a" : (21, {"c":2}),
   "b" : (19, {"c":13}),
   "c" : (19, {"d":5, "e":4, "f":8}),
   "d" : (9, {"f":5}),
   "e" : (11, {"f":7}),
   "f" : (12, {"g":8, "h":7, "z":18}),
   "g" : (4, {"z":9}),
   "h" : (6, {"z":6}),
   "z" : (0, {})
}
g = graph(graph_elements)

# as listed in the question, the search function
def search(priority_func, frontier_pop, front_append, graph, start, goal, start_val):
    frontier = [([start], 0, start_val)]   #frontier contains path and its cost, and any extra value needed
    while frontier:
        frontier = priority_func(frontier) # this is mainly if we want to use a frontier that prioritises one thing or the other
        path, path_cost, val = frontier_pop(frontier)
        curr = path[-1]
        if curr == goal: 
            return path, path_cost
        frontier.extend(front_append(curr,graph,  path, path_cost, val))# add paths and its relevant things to the frontier 
    return None, None


def DFS_front_append(curr, graph, path, path_cost, val):
    neighb = graph.get_neighbours_cost(curr) # returns dict 
    nodes = list(neighb.keys())
    costs = list(neighb.values())
    result = []
    # need to add the lists in reverse so stack pops it in alphabetical order
    for i in range(1,len(nodes)+1): 
        new_path = path.copy()
        new_path.append(nodes[-i])
        new_path_cost  = path_cost + costs[-i]
        result.append((new_path, new_path_cost,0)) # no third value to be considered
    return result

def BFS_front_append(curr, graph, path, path_cost, val):
    neighb = graph.get_neighbours_cost(curr) # returns dict 
    result = []
    for node, cost in neighb.items():
        new_path = path.copy()
        new_path.append(node)
        new_path_cost  = path_cost +  cost
        result.append((new_path, new_path_cost, 0)) # no third value to be considered
    return result

def BestFS_front_append(curr, graph, path, path_cost, val):
    neighb = graph.get_neighbours_cost(curr) # returns dict 
    result = []
    for node, cost in neighb.items():
        new_path = path.copy()
        new_path.append(node)
        new_path_cost  = path_cost +  cost
        result.append((new_path, new_path_cost, 
                       graph.get_heuristic(node))) # considers heuristics
    return result

def Astar_front_append(curr, graph, path, path_cost, val):
    neighb = graph.get_neighbours_cost(curr) # returns dict 
    result = []
    for node, cost in neighb.items():
        new_path = path.copy()
        new_path.append(node)
        new_path_cost  = path_cost +  cost
        result.append((new_path, new_path_cost, 
                       new_path_cost + graph.get_heuristic(node))) # considers f(p) = cost + heuristic
    return result

def IDS_front_append(curr, graph, path, path_cost, depth_left):
    neighb = graph.get_neighbours_cost(curr)
    nodes = list(neighb.keys())
    costs = list(neighb.values())
    result = []
    
    for i in range(1, len(nodes) + 1):
        new_path = path.copy()
        new_path.append(nodes[-i])
        new_path_cost = path_cost + costs[-i]
        if depth_left > 0:
            result.append((new_path, new_path_cost, depth_left - 1))  # Decrement depth limit for each path
        else:
            return result  # Depth limit reached, return an empty list
        
    return result

def IDS(g, start, goal):
    depth = 1
    result, result_cost = None, None
    while result == None and depth < 100:
        result, result_cost = search(lambda x: x, lambda x: x.pop(), IDS_front_append, g, start, goal, depth)
        depth += 1
    return result, result_cost

import numpy as np # only for setting UB = infty

def BandB(g, start, goal):
    start_val = g.get_heuristic(start)
    # starting values for upper bound and best solution
    UB  = np.inf
    best_path, best_cost = None, None

    frontier = [([start], 0, start_val)]   #frontier contains path and its cost, and f_value
    nodes_expanded = []
    temp  = 0
    while frontier:

        path, path_cost, f_value = frontier.pop()
        # B&B checking for lower UB
        while f_value > UB:
            # if frontier is empty and no more paths to consider
            if not frontier: return best_path, best_cost
            path, path_cost, f_value = frontier.pop()
        
        curr = path[-1]
        nodes_expanded.append(curr) 
        if curr == goal:
            best_path, best_cost = path, path_cost
            UB = best_cost # update UB
        
        neighb = g.get_neighbours_cost(curr) # returns dict 
        nodes = list(neighb.keys())
        costs = list(neighb.values())
        result = []
        # need to add the lists in reverse so stack pops it in alphabetical order
        for i in range(1,len(nodes)+1): 
            new_path = path.copy()
            new_path.append(nodes[-i])
            new_path_cost  = path_cost + costs[-i]
            result.append((new_path, 
                new_path_cost,new_path_cost + g.get_heuristic(nodes[-i]))) 
        frontier.extend(result)

    # no solution found
    return best_path, best_cost




# DFS uses stack
print("DFS search: ", 
        search(lambda x: x, lambda x: x.pop(), 
        DFS_front_append, g, "s", "z", 0))

#BFS uses queue
print("BFS search: ", 
        search(lambda x: x, lambda x: x.pop(0), 
        BFS_front_append, g, "s", "z",0))

# same as BFS but prioritises according to costs stored at index 1 in each element in frontier
print("LCFS search: ", 
        search(lambda x: sorted(x, key=lambda x:x[1]), lambda x: x.pop(0),
        BFS_front_append, g, "s", "z", 0))

# same as LCFS but prioritises according to heuristics stored at index 2 in each element in frontier
print("BestFS search: ", 
        search(lambda x: sorted(x, key=lambda x:x[2]), lambda x: x.pop(0),
        BestFS_front_append, g, "s", "z", g.get_heuristic("s")))

# same as LCFS but prioritises according to f(p) stored at index 2 in each element in frontier
print("Astar search: ", 
        search(lambda x: sorted(x, key=lambda x:x[2]), lambda x: x.pop(0), 
        Astar_front_append, g, "s", "z", g.get_heuristic("s") ))

# same as DFS but uses depth_left as its value which allows it to do iterative depth bound searches
print("IDS search: ", IDS(g, "s", "z"))

# same as DFS with informed f_values upper bound checking
print("B&B search:", BandB(g, "s", "z"))


