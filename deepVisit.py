graph = {1:[2,3],2:[4,5],3:[2],4:[1]}
visit = dict.fromkeys(list(range(6)),False)

stack = []

"""下面函数实现了以指定点为起点的（链表形式存储的）有向图的深度遍历

输入：遍历起始点
输出：起始点对于图中每个点的可达性

"""

def DFS(v):
    global graph
    global visit

    if visit[v] == True:
        return True
    visit[v] = True

    if graph.__contains__(v):
        for i in graph[v]:
            DFS(i)

DFS(2)
for i in visit.items():
    print(i)
