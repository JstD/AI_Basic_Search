from State import State
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue


#Depth-first Search with limited depth

 
def DFS(given_state , n):
    frontier = PriorityQueue()
    explored = [] 
    counter = 0
    root = State(given_state, None, None, 0, 0, n)
    #root.evaluation()
    evaluation = root.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
    frontier.put((evaluation, counter, root)) #based on bestFS evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(),current_node.current_state(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
                frontier.put((evaluation, counter, child)) #based on bestFS evaluation
    return

