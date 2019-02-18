"""
题目背景
　　小明是汉东省政法大学附属中学的一名学生，他每天都要骑自行车往返于家和学校。为了能尽可能充足地睡眠，他希望能够预计自己上学所需要的时间。他上学需要经过数段道路，相邻两段道路之间设有至多一盏红绿灯。
　　京州市的红绿灯是这样工作的：每盏红绿灯有红、黄、绿三盏灯和一个能够显示倒计时的显示牌。假设红绿灯被设定为红灯 r 秒，黄灯 y 秒，绿灯 g 秒，那么从 0 时刻起，[0,r) 秒内亮红灯，车辆不许通过；[r, r+g) 秒内亮绿灯，车辆允许通过；[r+g, r+g+y) 秒内亮黄灯，车辆不许通过，然后依次循环。倒计时的显示牌上显示的数字 l（l > 0）是指距离下一次信号灯变化的秒数。
问题描述
　　一次上学的路上，小明记录下了经过每段路的时间，和各个红绿灯在小明到达路口时的颜色和倒计时秒数。希望你帮忙计算此次小明上学所用的时间。
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
        elif type == 1:
            total_time += count
        elif type == 2:
            total_time += count + r
    print(total_time)
