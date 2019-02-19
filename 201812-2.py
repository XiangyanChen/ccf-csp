"""
题目背景
　　汉东省政法大学附属中学所在的光明区最近实施了名为“智慧光明”的智慧城市项目。具体到交通领域，通过“智慧光明”终端，可以看到光明区所有红绿灯此时此刻的状态。小明的学校也安装了“智慧光明”终端，小明想利用这个终端给出的信息，估算自己放学回到家的时间。
问题描述
　　一次放学的时候，小明已经规划好了自己回家的路线，并且能够预测经过各个路段的时间。同时，小明通过学校里安装的“智慧光明”终端，看到了出发时刻路上经过的所有红绿灯的指示状态。请帮忙计算小明此次回家所需要的时间。
"""

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    n = int(input())
    r = input_list[0]
    y = input_list[1]
    g = input_list[2]
    total_time = 0
    for i in range(n):
        input_list = list(map(int, input().split()))
        type = input_list[0]
        count = input_list[1]
        if type == 0:
            total_time += count
            # print("用时%d秒"%count)
        else:
            now = 0
            if type == 1:
                now = (r - count + total_time) % (r+y+g)
            elif type == 2:
                now = (r + g + y - count + total_time) % (r+y+g)
            elif type == 3:
                now = (r + g - count + total_time) % (r+y+g)
            pre_total_time = total_time
            if (now < r):
                total_time += r - now
                # print(r - now)
            elif (now >= r + g and now < r + g + y):
                total_time += r + g + y - now + r
                # print(r + g + y - now + r)
            # print("用时%d秒" % (total_time-pre_total_time))
    print(total_time)