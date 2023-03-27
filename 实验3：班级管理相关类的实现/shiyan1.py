# 实验三
class preson:
    name = ''
    age = 0
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __call__(self, *args, **kwargs):
        print("被调用")
    def sleep(self):
        print(f"今年{self.age}的{self.name}在睡觉")
    def eat(self):
        print(f"今年{self.age}的{self.name}在吃饭")
class student(preson):
    xuehao=1936
    def __init__(self,n,a,x):
        preson.__init__(self, n, a)
        self.xuehao=x
    def __call__(self, *args, **kwargs):
        preson.__call__(self,*args, **kwargs)
    def sleep(self):
        preson.sleep(self)
    def eat(self):
        preson.eat(self)
    def study(self):
        print(f"今年{self.age},学号为{self.xuehao}的{self.name}正在学习")

class zuzhang(student):
    zhiwu=''
    def __init__(self,n,a,x,z):
        student.__init__(self,n,a,x)
        self.zhiwu=z
    def __call__(self, *args, **kwargs):
        preson.__call__(self,*args, **kwargs)
    def sleep(self):
        student.sleep(self)
    def eat(self):
        student.eat(self)
    def guanli(self):
        print(f"今年{self.age},学号为{self.xuehao}的{self.name}正在管理，这就是某班的{self.zhiwu}")
class teacher(preson):
    zhiwu=''
    def __init__(self, n, a, z):
        preson.__init__(self, n, a)
        self.zhiwu=z
    def __call__(self, *args, **kwargs):
        preson.__call__(self,*args, **kwargs)
    def sleep(self):
        preson.sleep(self)
    def eat(self):
        preson.eat(self)
    def jiaoxue(self):
        print(f"今年{self.age}的{self.zhiwu}{self.name}正在用清脆的嗓音教导学生")
    def guanli(self):
        print(f"今年{self.age}的{self.zhiwu}{self.name}正在管理")
print("学生")
s=student('小明',12,1937)
print("使用魔法方法:")
s()
print("使用类里面方法:")
s.eat()
s.sleep()
s.study()
print("组长")
z=zuzhang('明明',13,1968,'组长')
print("使用魔法方法:")
z()
print("使用类里面方法:")
z.sleep()
z.eat()
z.guanli()
print("教师")
t=teacher('李老师',36,'教导主任')
print("使用魔法方法:")
t()
print("使用类里面方法:")
t.sleep()
t.eat()
t.guanli()
t.jiaoxue()