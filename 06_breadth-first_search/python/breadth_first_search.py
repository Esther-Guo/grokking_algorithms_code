from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = deque() # queue
search_queue += graph["you"]
searched = []
def mango_seller(name):
    if name[-1]=="m":
        return True
    else:
        return False

def bfs(search_queue):
    while search_queue:
        person = search_queue.popleft()
        if person not in searched: # avoid repeated search for the same person
            if mango_seller(person) == True:
                print(f"{person} is the mango seller!")
                return
            else:
                searched.append(person)
                search_queue += graph[person]

    print("can't find any mango seller")
    return

bfs(search_queue)