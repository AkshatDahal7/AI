#Discussed with Indra(102203123)
import copy
q = []
visited = []
g = [[1,2,3],[8,0,4],[7,6,5]]
s = [[2,8,3],[1,5,4],[7,6,0]]    

def manhatten(s):
    x = 0
    global g
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] != g[i][j]:
                x+=1
    return x

def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j]==0:
                return [i,j]
 
def up(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if x>0:
        s1[x][y] = s1[x-1][y]
        s1[x-1][y] = 0
    return s1    
 
def down(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if x<2:
        s1[x][y] = s1[x+1][y]
        s1[x+1][y] = 0
    return s1
 
def left(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if y>0:
        s1[x][y] = s1[x][y-1]
        s1[x][y-1] = 0
    return s1    
 
def right(s):
    s1 = copy.deepcopy(s)
    pos = find_pos(s)
    x = pos[0]
    y = pos[1]
 
    if y<2:
        s1[x][y] = s1[x][y+1]
        s1[x][y+1] = 0
    return s1  
 
def generate_child(s):
    global q
    global visited
    global g
    
    new_state = up(s)
    dis = manhatten(new_state)
    if [dis,new_state,s] not in q and [dis,new_state,s] not in visited and new_state!=s:
        q.append([dis,new_state,s]) 
    new_state = down(s)
    dis = manhatten(new_state)
    if [dis,new_state,s] not in q and [dis,new_state,s] not in visited and new_state!=s:
        q.append([dis,new_state,s])     
    new_state = left(s)
    dis = manhatten(new_state)
    if [dis,new_state,s] not in q and [dis,new_state,s] not in visited and new_state!=s:
        q.append([dis,new_state,s])     
    new_state = right(s)
    dis = manhatten(new_state)
    if [dis,new_state,s] not in q and [dis,new_state,s] not in visited and new_state!=s:
        q.append([dis,new_state,s])    
 
def search(g):
    global q
    global visited
    global s
    c = 0

    while len(q):
        q.sort()

        best_state = q[0][1]
        parent = q[0][2]

        q.clear()
        c+=1

        if best_state==g:
            print(f"Found in {c} steps")
            exit()
        
        generate_child(best_state)
        visited.append([manhatten(best_state),best_state,parent])
        
        print(c)
    print("Cannot Find Solution")
    exit()

def main():
    global q
    global g
    global s    
    
    q.append([manhatten(s),s,s])
    search(g)
 
main()