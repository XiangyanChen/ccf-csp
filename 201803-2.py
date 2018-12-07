"""
问题描述
　　数轴上有一条长度为L（L为偶数)的线段，左端点在原点，右端点在坐标L处。有n个不计体积的小球在线段上，开始时所有的小球都处在偶数坐标上，速度方向向右，速度大小为1单位长度每秒。
　　当小球到达线段的端点（左端点或右端点）的时候，会立即向相反的方向移动，速度大小仍然为原来大小。
　　当两个小球撞到一起的时候，两个小球会分别向与自己原来移动的方向相反的方向，以原来的速度大小继续移动。
　　现在，告诉你线段的长度L，小球数量n，以及n个小球的初始位置，请你计算t秒之后，各个小球的位置。
提示
　　因为所有小球的初始位置都为偶数，而且线段的长度为偶数，可以证明，不会有三个小球同时相撞，小球到达线段端点以及小球之间的碰撞时刻均为整数。
　　同时也可以证明两个小球发生碰撞的位置一定是整数（但不一定是偶数）。
输入格式
　　输入的第一行包含三个整数n, L, t，用空格分隔，分别表示小球的个数、线段长度和你需要计算t秒之后小球的位置。
　　第二行包含n个整数a1, a2, …, an，用空格分隔，表示初始时刻n个小球的位置。
输出格式
　　输出一行包含n个整数，用空格分隔，第i个整数代表初始时刻位于ai的小球，在t秒之后的位置。
样例输入
3 10 5
4 6 8
样例输出
7 9 9
"""
import copy

class Ball:
    def __init__(self, id, action):
        self.id = id
        self.action = action
        self.index = 0
    def set_action(self, action):
        self.action = action

    def get_action(self):
        return self.action

    def get_id(self):
        return self.id

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def __str__(self):
        return str(self.id)
if __name__ == "__main__":
    first_line_list = list(map(int, input().split()))
    n = first_line_list[0]  #the number of balls
    length = first_line_list[1]
    seconds = first_line_list[2] #seconds
    num_list = list(map(int, input().split()))
    number_axis = [list() for i in range(length)]
    ball_list = [Ball(i, "right") for i in range(n)]
    for index,num in enumerate(num_list):
        ball = ball_list[index]
        ball.set_index(num-1)
        number_axis[num-1].append(ball)
    for second in range(seconds+2):
        temp_number_axis = [list() for i in range(length)]
        for index, element in enumerate(number_axis):
            if (len(element) == 1):
                ball = element[0]
                if (ball.get_action() == "left"):
                    temp_number_axis[index-1].append(ball)
                    ball.set_index(index-1)
                else:
                    temp_number_axis[index+1].append(ball)
                    ball.set_index(index+1)
            elif (len(element) >= 2):
                for ball in element:
                    if (ball.get_action() == "left"):
                        temp_number_axis[index+1].append(ball)
                        ball.set_index(index+1)
                        ball.set_action("right")
                    else:
                        temp_number_axis[index-1].append(ball)
                        ball.set_index(index-1)
                        ball.set_action("left")
        element = temp_number_axis[0]
        if (len(element) > 0):
            for ball in element:
                ball.set_action("right")
        element = temp_number_axis[length-1]
        if (len(element) > 0):
            for ball in element:
                ball.set_action("left")
        number_axis = temp_number_axis
        for element in number_axis:
            if (len(element) >= 1):
                print("[", end=" ")
                for x in element:
                    print(x, end=" ")
                print(']', end=" ")
            else:
                print("[ ]", end=" ")
        print()
        # for ball in ball_list:
        #     print(ball.get_index()+1, end=" ")
    for ball in ball_list:
        print(ball.get_index()+1, end=" ")
