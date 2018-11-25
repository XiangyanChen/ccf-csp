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

if __name__ == "__main__":
    num_list = (list(map(int, input().split())))
    n = num_list[0]
    m = num_list[1]
    line_list = list()
    selector_list = list()
    for i in range(n):
        line_list.append(input())
    for i in range(m):
        selector_list.append(input())
    # for line in line_list:
    #     print(line)
    for selector in selector_list:
        index_list = list()
        for index, line in enumerate(line_list):
            line = line.replace(".", "")
            if selector in line.split(" "):
                index_list.append(index)
        print(len(index_list), end=" ")
        for index in index_list:
            print("%d" % (index + 1), end=" ")
        print()
