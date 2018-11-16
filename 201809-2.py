
if __name__ == "__main__":
    input_n = int(input())
    count_list = [0] * 1000000
    for i in range(input_n * 2):
        split_num = list(map(int, input().split()))
        left = split_num[0] #左闭区间
        right = split_num[1]    #右闭区间
        for i in range(left-1, right-1):
            count_list[i] += 1
    print(count_list.count(2))
