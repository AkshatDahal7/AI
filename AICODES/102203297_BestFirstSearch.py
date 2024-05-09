import copy
q = []
visited = []
g = [[1,2,3],[8,0,4],[7,6,5]]

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
    if [dis,new_state] not in q and [dis,new_state] not in visited:
        q.append([dis,new_state]) 
    new_state = down(s)
    dis = manhatten(new_state)
    if [dis,new_state] not in q and [dis,new_state] not in visited:
        q.append([dis,new_state])     
    new_state = left(s)
    dis = manhatten(new_state)
    if [dis,new_state] not in q and [dis,new_state] not in visited:
        q.append([dis,new_state])     
    new_state = right(s)
    dis = manhatten(new_state)
    if [dis,new_state] not in q and [dis,new_state] not in visited:
        q.append([dis,new_state])    
 
def search(g):
    global q
    global visited
    c = 0
 
    while len(q):
        q.sort()
        cur = q[0][1]
        p = q[0]
        del q[0]
        c+=1

        if cur==g:
            print(f"Found in {c} steps")
            exit()
        
        generate_child(cur)
        visited.append(p)
        print(c)
    print("Cannot Find Solution")
    exit()

def main():
    global q
    global g
    s = [[2,8,3],[1,5,4],[7,6,0]]        
    
    q.append([manhatten(s),s])
    search(g)
 
main()