graph = {1:[2,3],2:[4,5],3:[2],4:[1]}
visit = dict.fromkeys(list(range(6)),False)

stack = []
flag = dict.fromkeys(list(range(6)),False)
numRecord = dict.fromkeys(list(range(6)),False)
def DFS(v):
    global graph
    global visit
    global stack
    global flag
    if visit[v] == True:
        return True
    visit[v] = True
    stack.append(v)
    if graph.__contains__(v):
        for i in graph[v]:
            if DFS(i):
                if stack.__contains__(i):
                    index = stack.index(i)
                    for i in range(index, len(stack)):
                        flag[stack[i]] = True
                        numRecord[i] = i

                elif numRecord[i] != False:
                    if stack.__contains__(numRecord[i]):
                        flag[v] = True
    stack.pop()

DFS(2)
for i in flag.items():
    print(i)