import functools
class IP:
    def __init__(self, ip_str):
        self.length = None  #前缀长度
        if "/" in ip_str:
            split_result = ip_str.split("/")
            self.length = int(split_result[1])
            ip_str = split_result[0]
        self.ip_digit_list = list(map(int, ip_str.split(".")))
        if (self.length == None):
            self.length = len(self.ip_digit_list) * 8
        for i in range(4-len(self.ip_digit_list)):
            self.ip_digit_list.append(0)
        self.ip_binary_list = list()
        for digit in self.ip_digit_list:
            self.ip_binary_list.append(digit2binary(digit))
        self.ip_address_str = ".".join(map(str, self.ip_digit_list))    #ip地址字符串
        self.ip_binary_str = "".join(self.ip_binary_list)   #32位2进制

    def __str__(self):
        return self.ip_address_str + "/" + str(self.length)

def digit2binary(digit):
    binary_str = ""
    digit = int(digit)
    while digit > 0:
        binary_str = str(digit % 2) + binary_str
        digit = int(digit / 2)
    for i in range(8 - len(binary_str)):  # 补全到8位
        binary_str = "0" + binary_str
    return binary_str
# def cmp1(list1, list2):
#     list1 = list1.ip_digit_list
#     list2 = list2.ip_digit_list
#     # print(list1)
#     # print(list2)
#     for x, y in zip(list1, list2):
#         if (x < y):
#             return -1
#         elif (x > y):
#             return 1
#     return 0
def is_merge(ip1, ip2):
    ip1_length = ip1.length
    ip2_length = ip2.length
    if ip1.length == ip2.length and ip1.ip_binary_str[ip1_length-1] != ip2.ip_binary_str[ip2_length-1] and ip1.ip_binary_str[:ip1_length-1] == ip2.ip_binary_str[:ip2_length-1]:
        return True
    else:
        return False
def convert2new_ip(ip1, ip2):   #构造新的ip
    if (ip1.ip_binary_str < ip2.ip_binary_str):
        return IP(ip1.ip_address_str + "/" + str(ip1.length-1))
    else:
        return IP(ip2.ip_address_str + "/" + str(ip2.length-1))
# ip_address  = ""
    # ip_binary_str = ip.ip_binary_str[:ip.length-1]
    # for i in range(4):
    #     sum =0
    #     for x in ip_binary_str[i * 8:(i+1) * 8]:
    #         sum = sum*2+int(x)
    #     ip_address += str(sum) + "."
    # return IP(ip_address[:-1] + "/" + str(ip.length-1))

if __name__ == "__main__":
    n = int(input())    #number of input
    ip_list = list()
    for i in range(n):
        # print()
        ip_str = str(input())
        try:
            ip = IP(ip_str) #标准化
            ip_list.append(ip)
        except:
            pass
    ip_list = sorted(ip_list, key=lambda x:x.length)    #第一步
    ip_list = sorted(ip_list, key=lambda x:x.ip_binary_str)
    # ip_list = sorted(ip_list, key=functools.cmp_to_key(cmp1))   #ip地址排序，ip分成数组
    new_ip_list = list()
    pre_ip = None
    for ip in ip_list:  #第二步
        if pre_ip == None:
            pre_ip = ip
            new_ip_list.append(pre_ip)
        else:
            match_result = ""
            for i in range(pre_ip.length):
                if (pre_ip.ip_binary_str[i] != ip.ip_binary_str[i]):
                    new_ip_list.append(ip)
                    pre_ip = ip
                    break
    ip_list = list()
    for ip in new_ip_list:  #第三步
        if (len(ip_list)) == 0:
            ip_list.append(ip)
        else:
            if (is_merge(ip_list[-1], ip)):
                new_ip = ip
                while (is_merge(ip_list[-1], new_ip)):
                    pre_ip = ip_list.pop()
                    new_ip = convert2new_ip(pre_ip, new_ip)
                    if (len(ip_list) == 0):
                        break
                ip_list.append(new_ip)
            else:
                ip_list.append(ip)
    #     if (len(ip_list)) == 0:
    #         ip_list.append(ip)
    #     else:
    #         if(is_merge(ip_list[-1], ip)):
    #             new_ip = IP(set_to_ip(ip.ip_binary_str[:ip.length-1])+ "/" + str(ip.length-1))
    #             # print(new_ip)
    #             pre_ip = ip_list.pop()
    #             if (len(ip_list) > 0):
    #                 while(is_merge(ip_list[-1], new_ip)):
    #                     pre_ip = ip_list.pop()
    #                     new_ip = IP(set_to_ip(new_ip.ip_binary_str[:new_ip.length-1]) + "/" + str(new_ip.length-1))
    #                     if (len(ip_list) == 0):
    #                         break
    #             ip_list.append(new_ip)
    #         else:
    #             ip_list.append(ip)
    for ip in ip_list:
        print(ip)