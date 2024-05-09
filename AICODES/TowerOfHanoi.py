#Tower of Hanoi
import copy
g = [[],[],['C','B','A']]
q = []
def cmp(s,g):
    return s==g

def generate_child_BFS(s):
    global q
    for i in range(len(s)):
        temp = copy.deepcopy(s)
        if(s[i]!=[]):
            x = temp[i][-1]
            del temp[i][-1]
            for j in range(len(s)):
                if i!=j:
                    newState = copy.deepcopy(temp)
                    newState[j] = newState[j] + [x]
                    if(newState not in q):
                        q.append(newState)

def generate_child_DFS(s):
    global q
    for i in range(len(s)):
        temp = copy.deepcopy(s)
        if(s[i]!=[]):
            x = temp[i][-1]
            del temp[i][-1]
            for j in range(len(s)):
                if i!=j:
                    newState = copy.deepcopy(temp)
                    newState[j] = newState[j] + [x]
                    if(newState not in q):
                        q.insert(0,newState)             

def solve(s):
    global g
    global q
    c = 0
    while len(q):
        cur = q[0]
        del q[0]
        c = c + 1
        if(cmp(cur,g)):
            print(f"Found in {c} steps")
            print(cur)
            exit()
        generate_child_BFS(cur)
    print("Not Found")
    exit()



def main():
    global q
    s = [['A'], ['B','C'], []]

    q.append(s)
    solve(s)

if __name__=='__main__':
    main()