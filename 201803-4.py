import copy
"""
　Alice和Bob正在玩井字棋游戏。
　　井字棋游戏的规则很简单：两人轮流往3*3的棋盘中放棋子，Alice放的是“X”，Bob放的是“O”，Alice执先。当同一种棋子占据一行、一列或一条对角线的三个格子时，游戏结束，该种棋子的持有者获胜。当棋盘被填满的时候，游戏结束，双方平手。
　　Alice设计了一种对棋局评分的方法：
　　- 对于Alice已经获胜的局面，评估得分为(棋盘上的空格子数+1)；
　　- 对于Bob已经获胜的局面，评估得分为 -(棋盘上的空格子数+1)；
　　- 对于平局的局面，评估得分为0；
"""
"""
3
1 2 1
2 1 2
0 0 0
2 1 1
0 2 1
0 0 2
0 0 0
0 0 0
0 0 0
"""
def is_win(chess):
    values = [1, 2]
    for x in values:
        line_list = list()
        for i in range(3):
            line_list.append([chess[i][0], chess[i][1], chess[i][2]])
            line_list.append([chess[0][i], chess[1][i], chess[2][i]])
        line_list.append([chess[0][0], chess[1][1], chess[2][2]])
        line_list.append([chess[0][2], chess[1][1], chess[2][0]])
        for line in line_list:
            if (line.count(x) == 3):
                if (x == 1):    #说明是Alice赢
                    return get_score(chess) + 1
                else:
                    return - get_score(chess) - 1
    return 0

def move(chess, num):
    # print(chess)
    score = get_score(chess)
    if (score == 0):
        return score
    max_value = -10
    min_value = 10
    for i in range(3):  #先找胜利方法
        for j in range(3):
            if (chess[i][j] == 0):
                # chess_ = copy.deepcopy(chess)
                chess_ = chess
                chess_[i][j] = num
                x = is_win(chess_)
                if (x != 0):
                    chess[i][j] = 0

                    if (num == 1):
                        return max(max_value, x)
                    else:
                        return min(min_value, x)
                if (num == 1):
                    max_value = max(max_value, move(chess_, 2))
                else:
                    min_value = min(min_value, move(chess_, 1))
                chess[i][j] = 0
    if (num == 1):
        return max_value
    else:
        return min_value

def get_score(chess):
    sum = 0  # 总数，用来检测此盘还可以走吗
    for part in chess:
        sum += part.count(0)
    return sum


if __name__ == "__main__":
    m = int(input())
    chess_list = list()
    for i in range(m):  #添加棋盘
        chess = list()
        for j in range(3):
            chess.append(list(map(int, input().split())))
        chess_list.append(chess)
    for chess in chess_list:
        x = is_win(chess)
        if (x != 0):    #开局就已经赢了
            print(x)
        else:
            print(move(chess, 1))
    # print(get_score(chess_list[2]))

    # for chess in chess_list:
    #     print(chess)

