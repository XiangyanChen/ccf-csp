"""

主要是使用kruskal算法
"""
class Arc:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    # def __str__(self):
    #     return "%d -> %d, %d" % (self.start, self.end, self.weight)
p = list()
sum = 0
count = 0
ans = -1
def find(x):
    if (p[x] == x):
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def union_set(start, end, weight):
    global sum
    global count
    global p
    global ans
    start = find(start)
    end = find(end)
    # print("%d and %d"%(start, end))
    if (start != end):
        # print(weight)
        p[start] = end
        sum += weight
        count += 1
        if (ans < weight):
            ans = weight

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    root = int(input())
    # graph = Graph(n, m, root)
    arc_list = list()
    for i in range(m):
        input_list = list(map(int, input().split()))
        start, end, weight = input_list[0], input_list[1], input_list[2]
        arc = Arc(start, end, weight)
        arc_list.append(arc)
    arc_list = sorted(arc_list, key=lambda x:x.weight)
    p.append(0)
    for i in range(n):
        p.append(i+1)
    for arc in arc_list:
        union_set(arc.start, arc.end, arc.weight)
    print(ans)
