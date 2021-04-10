from Search_Algorithms import DFS #BFS, DFS, Greedy, AStar_search
import random
#initial state
n = int(input("Enter n\n"))
print("Enter your" ,n,"*",n, "puzzle")
def num_of_invers(lst,n):
    num_of_invers = 0
    for i in range(n*n):
        if lst[i] ==0:
            continue
        for j in range(i,n*n,1):
            if lst[j]!=0 and lst[j]<lst[i]:
                num_of_invers +=1
    return num_of_invers

def is_good_init(lst,n):
    '''If N is odd, then puzzle instance is solvable 
    if number of inversions is even in the input state.'''
    if n%2==1:
        return num_of_invers(lst,n)%2==0
    else:
        """If N is even, puzzle instance is solvable if 
                +) the blank is on an even row counting from the bottom 
            (second-last, fourth-last, etc.) and number of inversions is odd.
                +) the blank is on an odd row counting from the bottom 
            (last, third-last, fifth-last, etc.) and number of inversions is even."""
        blanks_rows_inverse = n - int(lst.index(0)/n)
        if blanks_rows_inverse%2==0:
            return num_of_invers(lst,n) %2 ==1
        else:
            return num_of_invers(lst,n)%2 ==0
    return False
def generate_init_solvable(n):
    while True:
        result = [x for x in range(n*n)]
        random.shuffle(result)
        if is_good_init(result,n):
            return result



root = generate_init_solvable(n)


print("The given state is:",root,"\n")
for x in range(n):
    print (root[x*n:x*n+n])



#count the number of inversions       
def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv

def solvable(puzzle): #check if initial state puzzle is solvable: number of inversions should be even.
    inv_counter = inv_num(puzzle)
    if (inv_counter %2 ==0):
        return True
    return False


#1,8,2,0,4,3,7,6,5 is solvable
#2,1,3,4,5,6,7,8,0 is not solvable

from time import time

if solvable(root):

    time2 = time()
    DFS_solution = DFS(root, n)
    DFS_time = time() - time2
    print('DFS Solution is ')
    for i in range(len(DFS_solution[0])):
        print(DFS_solution[0][i],' ',DFS_solution[1][i],"\n")
        for x in range(n):
            print (DFS_solution[1][i][x*n:x*n+n])

        print("\n")    

    print('Number of explored nodes is ', DFS_solution[2])
    print('DFS Time:', DFS_time, "\n")  



    
else:
    print("Not solvable")



     