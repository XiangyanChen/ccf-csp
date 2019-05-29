"""
　　URL 映射是诸如 Django、Ruby on Rails 等网页框架 (web frameworks) 的一个重要组件。对于从浏览器发来的 HTTP 请求，URL 映射模块会解析请求中的 URL 地址，并将其分派给相应的处理代码。现在，请你来实现一个简单的 URL 映射功能。
　　本题中 URL 映射功能的配置由若干条 URL 映射规则组成。当一个请求到达时，URL 映射功能会将请求中的 URL 地址按照配置的先后顺序逐一与这些规则进行匹配。当遇到第一条完全匹配的规则时，匹配成功，得到匹配的规则以及匹配的参数。若不能匹配任何一条规则，则匹配失败。
　　本题输入的 URL 地址是以斜杠 / 作为分隔符的路径，保证以斜杠开头。其他合法字符还包括大小写英文字母、阿拉伯数字、减号 -、下划线 _ 和小数点 .。例如，/person/123/ 是一个合法的 URL 地址，而 /person/123? 则不合法（存在不合法的字符问号 ?）。另外，英文字母区分大小写，因此 /case/ 和 /CAse/ 是不同的 URL 地址。
　　对于 URL 映射规则，同样是以斜杠开始。除了可以是正常的 URL 地址外，还可以包含参数，有以下 3 种：
　　字符串 <str>：用于匹配一段字符串，注意字符串里不能包含斜杠。例如，abcde0123。
　　整数 <int>：用于匹配一个不带符号的整数，全部由阿拉伯数字组成。例如，01234。
　　路径 <path>：用于匹配一段字符串，字符串可以包含斜杠。例如，abcd/0123/。
　　以上 3 种参数都必须匹配非空的字符串。简便起见，题目规定规则中 <str> 和 <int> 前面一定是斜杠，后面要么是斜杠，要么是规则的结束（也就是该参数是规则的最后一部分）。而 <path> 的前面一定是斜杠，后面一定是规则的结束。无论是 URL 地址还是规则，都不会出现连续的斜杠。
"""
"""
    5 4
    /articles/2003/ special_case_2003
    /articles/<int>/ year_archive
    /articles/<int>/<int>/ month_archive
    /articles/<int>/<int>/<str>/ article_detail
    /static/<path> static_serve
    /articles/2004/
    /articles/1985/09/aloha/
    /articles/hello/
    /static/js/jquery.js
"""

class Matcher():
    def __init__(self, rule, name):
        self._rule = rule
        self._name = name

    @property
    def rule(self):
        return self._rule

    @property
    def name(self):
        return self._name

if __name__ == "__main__":
    num_list = (list(map(int, input().split())))
    n = num_list[0] #文档n行
    m = num_list[1] #需要检测的m行
    matcher_list = list()
    for i in range(n):
        rule, name = input().split()
        matcher_list.append(Matcher(rule, name))    #添加规则
    # print(matcher_list)
    data_list = list()
    for i in range(m):  #每条匹配
        source = input()

        results = source.split("/")
        for mathcer in matcher_list:
            param_list = list()
            rule_list = mathcer.rule.split("/")
            i = 0
            flag = True
            path_flag = False
            while (i < len(results) and i < len(rule_list)):
                rule = rule_list[i]
                result = results[i]
                i += 1
                if rule == "<int>":
                    if result.isdigit():
                        if (int(result) != 0):
                            param_list.append(str(int(result)))

                        continue
                    else:
                        flag = False
                        break
                elif rule == "<str>":
                    param_list.append(result)
                    continue
                elif rule == "<path>":
                    index = 0
                    for j in range(i-1):
                        index = source.index("/", index)
                        index += 1
                    path_flag = True
                    param_list.append(source[index:])
                    # param_list.append("/".join(results[index:]))
                    break
                elif (rule != result):
                    flag = False

                    break
                #i += 1
            if (i < len(results)):
                 flag = False
            #     data_list.append("404")
            #     break
            if (i < len(rule_list)):
                 flag = False
            #     data_list.append("404")
            #     break
            if (flag == True or path_flag == True):
                data_list.append(mathcer.name + " " + " ".join(param_list))
                break
        else:
            data_list.append("404")
            # print("404")
    for data in data_list:
        print(data)