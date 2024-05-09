import sys
import copy

q=[]
visited=[]

def enqueue(s,val):
    global q

    q = q + [(val,s)]

def herusitic(s,g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j]!=g[i][j]:
                d+=1
    return d

def dequeue():

    global q
    global visited

    q.sort()
    visited = visited + [q[0][1]]
    q.sort()
    elem = q[0]
    del q[0]
    return (elem)

def find_pos(state):

    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return ([i,j])

def up(state,pos):

    i = pos[0]
    j = pos[1]
    if i>0:
        temp = copy.deepcopy(state)
        temp[i][j] = temp[i-1][j]
        temp[i-1][j] = 0
        return (temp)
    else:
        return (state)

def down(state,pos):

    i = pos[0]
    j = pos[1]
    if i<2:
        temp = copy.deepcopy(state)
        temp[i][j] = temp[i+1][j]
        temp[i+1][j] = 0
        return (temp)
    else:
        return (state)


def left(state,pos):

    i = pos[0]
    j = pos[1]
    if j>0:
        temp = copy.deepcopy(state)
        temp[i][j] = temp[i][j-1]
        temp[i][j-1] = 0
        return (temp)
    else:
        return (state)

def right(state,pos):

    i = pos[0]
    j = pos[1]
    if j<2:
        temp = copy.deepcopy(state)
        temp[i][j] = temp[i][j+1]
        temp[i][j+1] = 0
        return (temp)
    else:
        return (state)

def search(s,g):
    curr_state = copy.deepcopy(s)

    if s==g:
        return
    global visited

    while(1):
        pos = find_pos(curr_state)
        new = up(curr_state,pos)
        if(new!=curr_state):
            if new==g:
                print("Found! The intermediate state are:")
                print(visited +[g])
                return
            else:
                if new not in visited:
                    enqueue(new,herusitic(s,new) +herusitic(new,g))

        new = down(curr_state,pos)
        if(new!=curr_state):
            if new==g:
                print("Found! The intermediate state are:")
                print(visited +[g])
                return
            else:
                if new not in visited:
                    enqueue(new,herusitic(s,new) +herusitic(new,g))

        new = left(curr_state,pos)
        if(new!=curr_state):
            if new==g:
                print("Found! The intermediate state are:")
                print(visited +[g])
                return
            else:
                if new not in visited:
                    enqueue(new,herusitic(s,new) +herusitic(new,g))

        new = right(curr_state,pos)
        if(new!=curr_state):
            if new==g:
                print("Found! The intermediate state are:")
                print(visited +[g])
                return
            else:
                if new not in visited:
                    enqueue(new, herusitic(s,new) +herusitic(new,g))
        
        if len(q) > 0:
            temp = dequeue()
            curr_state = temp[1]
        else:
            print("not found!")
            return
        

def main():
    s = [[1,2,3],[4,0,6],[7,5,8]]
    g = [[1,2,3],[4,5,6],[7,8,0]]
    global q
    global visited
    q = q
    visited = visited + [s]
    search(s,g)

if __name__ == '__main__':
    main()