#based on sample code, less neat

# graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# cost table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def getNearestNode():
    length = infinity
    for node in costs.keys():
        if node not in processed and (costs[node]<length):
            length = costs[node]
            nearestNode = node
    if length == infinity:
        nearestNode = None
    return nearestNode

nearest = getNearestNode()
while nearest is not None:
    if nearest not in processed:
        neightbors = graph[nearest]
        for j in neightbors.keys():
            newcost = costs[nearest] + graph[nearest][j]
            if costs[j] > newcost:
                costs[j] = newcost
                parents[j] = nearest 
        processed.append(nearest)
    nearest = getNearestNode()
print(parents)
print(costs)