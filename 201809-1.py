

if __name__ == "__main__":
    input_num = int(input())
    num_list = (list(map(int, input().split())))
    new_num_list = [0 for i in range(len(num_list))]
    for i in range(len(num_list)):
        if i == 0:	#first store
            new_num_list[i] = int((num_list[i]  + num_list[i+1]) / 2)
        elif i == len(num_list) - 1:	#lass store
            new_num_list[i] = int((num_list[i-1] + num_list[i]) / 2)
        else:
            new_num_list[i] = int((num_list[i - 1] + num_list[i] + num_list[i+1]) / 3)
    print(" ".join([str(num) for num in new_num_list]))