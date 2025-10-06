from collections import deque

# Sample graph
graph = {
    'you': ['alice', 'bob', 'claire'],
    'alice': ['peggy'],
    'bob': ['anuj', 'peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}

# Function to check if a person is a mango seller
def is_mango_seller(name):
    return name[-1] == 'm'  # Example: someone whose name ends with 'm'

# BFS algorithm
def bfs(name):
    search_queue = deque(graph[name])
    searched = set()  # To keep track of searched people

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_mango_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue.extend(graph[person])
                searched.add(person)
    print("No mango seller found.")
    return False

# Run the search
bfs('you')
