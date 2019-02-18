'''
11 5
html
..head
....title
..body
....h1
....p #subtitle
....div #main
......h2
......p #one
......div
........p #two
p
#subtitle
h3
div p
div div p
'''
import re
class Node:
    def __init__(self, rank, element_name, id_name):
        self.rank = rank
        self.element_name = element_name
        self.id_name = id_name
    def __str__(self):
        return "rank:%d, element_name:%s, id_name:%s" % (self.rank, self.element_name, self.id_name)

if __name__ == "__main__":
    num_list = (list(map(int, input().split())))
    n = num_list[0]
    m = num_list[1]
    line_list = list()
    selector_list = list()
    node_list = list()
    for i in range(n):
        line = input().strip()
        line_list.append(line)
        dot_str = re.match("^\.*", line).group()
        line = line.replace(dot_str, "")
        try:
            node = Node((len(dot_str) + 2)/ 2, line.split()[0].lower(), line.split()[1].lower())
        except:
            node = Node((len(dot_str) + 2)/ 2, line.split()[0].lower(), None)
        node_list.append(node)
    for i in range(m):
        selector_list.append(input())
    for node in node_list:
        print(node)
    # for line in line_list:
    #     print(line)
    # for selector in selector_list:
    #     index_list = list()
    #     for index, line in enumerate(line_list):
    #         line = line.replace(".", "")
    #         if selector in line.split(" "):
    #             index_list.append(index)
    #     print(len(index_list), end=" ")
    #     for index in index_list:
    #         print("%d" % (index + 1), end=" ")
    #     print()
