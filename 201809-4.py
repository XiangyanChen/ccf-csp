"""
问题描述
　　在一条街上有n个卖菜的商店，按1至n的顺序排成一排，这些商店都卖一种蔬菜。
　　第一天，每个商店都自己定了一个正整数的价格。店主们希望自己的菜价和其他商店的一致，第二天，每一家商店都会根据他自己和相邻商店的价格调整自己的价格。具体的，每家商店都会将第二天的菜价设置为自己和相邻商店第一天菜价的平均值（用去尾法取整）。
　　注意，编号为1的商店只有一个相邻的商店2，编号为n的商店只有一个相邻的商店n-1，其他编号为i的商店有两个相邻的商店i-1和i+1。
　　给定第二天各个商店的菜价，可能存在不同的符合要求的第一天的菜价，请找到符合要求的第一天菜价中字典序最小的一种。
　　字典序大小的定义：对于两个不同的价格序列(a1, a2, ..., an)和(b1, b2, b3, ..., bn)，若存在i (i>=1), 使得ai<bi，且对于所有j<i，aj=bj，则认为第一个序列的字典序小于第二个序列。
输入格式
　　输入的第一行包含一个整数n，表示商店的数量。
　　第二行包含n个正整数，依次表示每个商店第二天的菜价。
输出格式
　　输出一行，包含n个正整数，依次表示每个商店第一天的菜价。
样例输入
8
2 2 1 3 4 9 10 13
样例输出
2 2 2 1 6 5 16 10
"""


def check(index, n, num_list, new_num_list):
    for i in range(200):
        if (index == n):
            if (int((new_num_list[-1] + new_num_list[-2]) / 2) == num_list[-1]):
                print(" ".join([str(x) for x in new_num_list]))
                return True
            elif (int((new_num_list[-1] + new_num_list[-2]) / 2) < num_list[-1]):
                new_num_list[index-1] += 1
                if (int((new_num_list[index - 2-1] + new_num_list[index - 1-1] + new_num_list[index-1]) / 3) > num_list[
                    index - 1-1]):
                    return False
                else:
                    continue
            else:
                return False
        if (index == 0):
            new_num_list[index] = i
            flag = check(index+1, n, num_list, new_num_list)
            if (flag == True):
                return True
            else:
                continue
        else:
            if (index == 1):
                new_num_list[index] = i
                if (int((new_num_list[index-1] + new_num_list[index]) / 2) < num_list[index-1]):
                    continue
                elif (int((new_num_list[index-1] + new_num_list[index]) / 2) > num_list[index-1]):
                    return False
                else:
                    flag = check(index + 1, n, num_list, new_num_list)
                    return flag
            else:
                new_num_list[index] = i
                if (int((new_num_list[index-2] + new_num_list[index-1] + new_num_list[index]) / 3) < num_list[index-1]):
                    continue
                elif (int((new_num_list[index-2] + new_num_list[index-1] + new_num_list[index]) / 3) > num_list[index-1]):
                    return False
                else:
                    flag = check(index + 1, n, num_list, new_num_list)
                    return flag
    return False

if __name__ == "__main__":
    n = int(input())    #The number of stores
    num_list = (list(map(int, input().split())))    #The list of second day price
    new_num_list = [-1] * n #The list of first day price
    check(0, n, num_list, new_num_list)
    # print(" ".join([str(x) for x in new_num_list]))
