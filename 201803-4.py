import copy

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
                return True
    return False

def move(chess, num):
    # print(chess)
    sum = 0 #总数，用来检测此盘还可以走吗
    for part in chess:
        sum += part.count(0)
    if (sum == 0):
        return 0
    if (is_win(chess)):
        if (num == 1):
            return -(sum+1)
        else:
            return sum+1
    flag = False    #安放棋子的flag
    for i in range(3):  #先找胜利方法
        if (flag):
            break
        for j in range(3):
            if (chess[i][j] == 0):
                chess_ = copy.deepcopy(chess)
                chess_[i][j] = num
                if (is_win(chess_)):
                    chess[i][j] = num
                    flag = True
                    break
    for i in range(3):  #再找躲避方法
        if (flag):
            break
        for j in range(3):
            if (chess[i][j] == 0):
                chess_ = copy.deepcopy(chess)
                if (num == 2):
                    chess_[i][j] = 1
                else:
                    chess_[i][j] = 2
                if (is_win(chess_)):
                    chess[i][j] = num
                    flag = True
                    break
    for i in range(3):  #随便放一个
        if (flag):
            break
        for j in range(3):
            if (chess[i][j] == 0):
                chess[i][j] = num
                flag = True
                break
    if (num == 1):
        x = move(chess, 2)
    else:
        x = move(chess, 1)
    return x

def get_score(chess):
    # return 0
    return move(chess, 1)


if __name__ == "__main__":
    m = int(input())
    chess_list = list()
    for i in range(m):  #添加棋盘
        chess = list()
        for j in range(3):
            chess.append(list(map(int, input().split())))
        chess_list.append(chess)
    for chess in chess_list:
        print(get_score(chess))
    # print(get_score(chess_list[2]))

    # for chess in chess_list:
    #     print(chess)

