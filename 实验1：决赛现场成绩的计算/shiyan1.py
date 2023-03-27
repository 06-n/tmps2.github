# 实验一
n=int(input())
if n<3:
    print("请重新输入")
else:
    d={}
    for i in range(1,n+1):
        m=int(input())
        # 判断范围
        if m<0|m>100:
            print("打分范围在0-100之间")
            break
        d[i]=m
    else:
        # print(d)
        # 去掉一个最高分和最低分
        # 去掉一个最高分
        for key,value in d.items():
            if (value==max(d.values())):
                del d[key]
                break
        # print(d)
        # 去掉一个最低分
        for key,value in d.items():
            if (value==min(d.values())):
                del d[key]
                break
        # print(d)
        sum=0
        for v in d.values():
            sum+=v
        else:
            print(sum/(len(d)))
