# 实验二

# 封装函数

# 判断字母
def iszimu(a):
    for site in a:
        if site.isalpha():
            break
    else:
        print("密码要求包含字母！")

# 判断数字
def isshuzi(a):
    for site in a:
        if site.isnumeric():
            break
    else:
        print("密码要求包含数字！")

# 判断强度
def isstr(a):
     str_level=0
     for site in x:
        if site.isalpha():
           str_level += 1
           break

     for site in x:
        if site.isnumeric():
            str_level += 1
            break

     if len(a)>=8:
         str_level+=1
     else:
         print("密码长度要求至少8位")
     print(f'密码强度为{str_level}')
     if str_level==3:
         print("恭喜！密码强度合格！")
     else:
         print("密码强度不合格")
     return str_level

# 执行
print("请输入密码:")
# 假定密码输入不得超过三次
for i in range(0,3):
    x = input()
    iszimu(x)
    isshuzi(x)
    isstr(x)
    if isstr(x)==3:
        break
else:
    print("次数达到上限")