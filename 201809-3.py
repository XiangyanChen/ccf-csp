"""
    A B C表示不同层级
"""
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
import copy
class Node:
    def __init__(self, line_id, rank, element_name, id_name):
        self.line_id = line_id
        self.rank = rank
        self.element_name = element_name
        self.id_name = id_name
    def __str__(self):
        return "rank:%d, element_name:%s, id_name:%s" % (self.rank, self.element_name, self.id_name)

if __name__ == "__main__":
    num_list = (list(map(int, input().split())))
    n = num_list[0] #文档n行
    m = num_list[1] #需要检测的m行
    line_list = list()
    selector_list = list()
    node_list = list()
    for i in range(n):
        line = input().strip()
        line_list.append(line)
        dot_str = re.match("^\.*", line).group()
        line = line.replace(dot_str, "")
        try:
            node = Node(i + 1, (len(dot_str) + 2) / 2, line.split()[0].lower(), line.split()[1])
        except:
            node = Node(i + 1, (len(dot_str) + 2) / 2, line.split()[0].lower(), None)
        node_list.append(node)
    for i in range(m):
        selector_list.append(input())
    for selector_input in selector_list:
        line_id_list = list()
        selector_list = selector_input.split(" ")
        #元素小写化，ID选择器不管
        for i in range(len(selector_list)):
            if ("#" not in selector_list[i]):
                selector_list[i] = selector_list[i].lower()
        if (len(selector_list) == 1):
            for node in node_list:
                if ("#" in selector_list[0]):
                    if (selector_list[0] == node.id_name):
                        line_id_list.append(node.line_id)
                else:
                    if (selector_list[0] == node.element_name):
                        line_id_list.append(node.line_id)
        else:
            selector_list.reverse() #旋转，自下向上的找选择题
            for node in node_list:
                if (("#" in selector_list[0] and node.id_name == selector_list[0]) or selector_list[0] == node.element_name):   #匹配到最下面的选择器，开始匹配上面的
                    temp_node_list = copy.deepcopy(node_list[:node_list.index(node)])
                    pre_rank = node.rank
                    i = 1
                    while (i < len(selector_list) and len(temp_node_list) != 0):    #从下自上一个一个匹配过去
                        temp_node = temp_node_list.pop()
                        if (("#" in selector_list[i] and temp_node.id_name == selector_list[i]) or selector_list[i] == temp_node.element_name):
                            if (temp_node.rank < pre_rank):
                                pre_rank = temp_node.rank
                                i += 1
                            else:
                                break
                        if (len(temp_node_list) == 0):  #遍历完文档还没匹配到，就是失败了
                            break
                    if (i == len(selector_list)):
                            # if (i == len(selector_split_result)):
                        line_id_list.append(node.line_id)
        print(str(len(line_id_list)) + " " + " ".join(map(str, line_id_list)))
