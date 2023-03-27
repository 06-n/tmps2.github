# 实验四
# ① books.txt：保存有一些书籍名称；
def books():
    text=input()
    file = open("books.txt", mode='a')
    file.write('\n'+text)
    file.close()


# ② users.txt：用于保存用户相关的信息；
# 用户注册的其他情况
def users(name,user):
    name1=name
    user1=user
    # with open('users.txt', mode='a+') as f:
    f=open('users.txt',mode='a+')
    for i in f:
        # 解释：默认strip()没有参数，则删除两侧的换行符和空格。
        line_new = i.strip()
        line_list = line_new.split('&')
        if line_list[0] == name1 and line_list[1] == user1:
            print("用户已经注册")
            break
    f.close()
    text = name1 + '&' + user1 + '\n'
    f.write(text)
    print("注册成功")
    f.close()

# ③ users_book.txt：记录哪些用户借了哪些书
def users_book(n,u,books):
    name=str(n)
    user=str(u)
    books=str(books)
    file=open("users_book.txt",mode='a')
    text=name+'&'+user+'&'+books+'\n'
    file.write(text)
    file.close()

# 查阅图书
def Look_book():
    file = open('books.txt', mode='r')
    for i in file:
        print(i)
    file.close()


# 借阅图书
def Jie_book(n,u):
    Look_book()
    with open('users_book.txt') as f:
        m=input("请选择你要借阅的图书")
        try:
            line = f.readline()
            line_new = line.rstrip()
            line_list = line_new.split('\n')
            # 判断输入的书是否已被借走
            if m not in line_list:
                # 借书之前先判断该用户之前是否借过，如果借过，就在后面累加图书
                for users_book in line_list:
                    if n in line_list:
                        ws = open('users_book.txt', mode='a')
                        if m in line_list[2]:
                            ws.write(n + '&' + u + '&' + m + '\n')
                            print("借书成功")
                            break
                        else:
                            print("您已借一本书，请重新选择")
                            break
                    else:
                        ws = open('users_book.txt', mode='a')
                        ws.write(n + '&' + u + '&' + m + '\n')
                        print("借书成功")
                        break
            else:
                print("图书已被借走")
        except Exception as err:
            print("错误原因：", err)

# 历史记录
def Li_shi(n,u):
    name = str(n)
    user = str(u)
    with open('users_book.txt', mode='r') as f:
        for line in f:
            line_new = line.strip()
            line_list = line_new.split('&')
            if name==line_list[0] and user==line_list[1]:
                print(line_list[2])

def xia_yi_bu(name,user):
    n=name
    u=user
    prompt = '''请选择
    1.查阅图书
    2.历史记录
    3.借阅书籍
    4.退出'''
    choise = input(prompt).strip()
    if choise=='1':
        print("以下为书籍")
        Look_book()
    elif choise=='2':
        print("历史记录")
        Li_shi(n, u)
    elif choise=='3':
        print("借阅图书")
        Jie_book(n,u)
    else:
        exit()

# 用户登录函数
def denglu(n,u):
    name=n
    user=u
    with open('users.txt','r') as f:
        for line in f:
            # 解释：默认strip()没有参数，则删除两侧的换行符和空格。
            line_new=line.strip()
            line_list=line_new.split('&')
            if line_list[0]==n and line_list[1]==u:
                print("登录成功")
                xia_yi_bu(name,user)

# 用户
if __name__ == '__main__':
     while 1:
        prompt = '''请选择
1.注册
2.登录
3.退出
请输入:'''
        choise = input(prompt).strip()
        if choise == '1':
            print('请输入用户名')
            n = str(input())
            print('请输入用户密码')
            u = str(input())
            users(n,u)
        elif choise == '2':
            print('请输入用户名')
            inm = input()
            print('请输入用户密码')
            iup = input()
            denglu(inm, iup)
        elif choise == '3':
            break