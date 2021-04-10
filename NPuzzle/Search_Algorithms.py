from State import State
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue


#Depth-first Search with limited depth

#Depth-first Search not heuristic function 
def DFS(given_state , n): 
    root = State(given_state, None, None, 0, 0, n)
    if root.test():
        return root.solution()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        max_depth = current_node.depth #current depth
        explored.append(current_node.state)
        check_ = False
        if max_depth == 10:
            continue #go to the next branch

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    check_ = True
                    return child.solution(),child.current_state(), len(explored), check_
                frontier.put(child)
    return (("Couldn't find solution in the limited depth."),0,len(explored),check_)

#Best-first Search has heuristic function 
# def BFS(given_state , n):
#     frontier = PriorityQueue()
#     explored = [] 
#     counter = 0
#     root = State(given_state, None, None, 0, 0, n)
#     evaluation = root.Manhattan_Distance(n) 
#     frontier.put((evaluation, counter, root)) #based on bestFS evaluation

#     while not frontier.empty():
#         current_node = frontier.get()
#         current_node = current_node[2]
#         explored.append(current_node.state)
        
#         if current_node.test():
#             return current_node.solution(),current_node.current_state(), len(explored)

#         children = current_node.expand(n)
#         for child in children:
#             if child.state not in explored:
#                 counter += 1
#                 evaluation = child.Manhattan_Distance(n) 
#                 frontier.put((evaluation, counter, child)) #based on bestFS evaluation
#     return

