# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。


s = input("请输入一个字符串：")
letter = 0
space = 0
digit = 0
others = 0
i = 0

while i < len(s):
    c = s[i]
    i += 1
    if c.isalpha():
        letter += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print("char=%d,space=%d,digit=%d,others=%d" % (letter, space, digit, others))


