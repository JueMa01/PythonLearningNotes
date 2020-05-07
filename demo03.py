"""                                    python的方法                      """
#python中一个项目包含的内容：
包-->模块-->类-->方法-->变量    #结构上，从前往后，由大到小，前者包含后者；但用法上，它们是同级别的，可以在一起使用  既包含又平等

#方法，也叫做函数，比如print()  len()  students.append()等等
对于print()这个方法/函数
方法名：print
参数：“括号里的内容”

"""
做一个“实现一个输入任意一个两位的数字，输出他们的和的方法”
"""
def jiafa(a,b):             #def是一个固定的格式，代表定义一个方法，如果定义一个类，前面就要用class
    """
    这个方法是实现一个输入任意一个两位的数字，输出他们的和的作用
    """
   
    print(a+b)

#使用做好的"加法函数”
jiafa(222,333)

#一般情况下，我们把做好的一系列函数/方法，放在一个专门的文件里，比如叫做func的文件，然后在其他地方要使用它，只需要在前面做好“导入方法的工作”即可
#方法的导入及使用：
#第1中导入方法的方式（有两种导入方法的方式）：
import func
func.jiafa(123,321)

#第2中导入方法的方式：
from func import jiafa
jiafa(123,321)

#包  
# python的包，包括系统自带的包和第三方的包，系统自带的，当电脑安装python时，自动的会安装这些包，这些包安装在python安装路径里的lib文件夹里，这些包可以在写python的程序中直接使用；  
#第三方的包  （注意，后面所有自动化的课程，几乎用的都是第三方的包）
#pip  是一个管理第三方包的工具
#pip常用的操作命令（要在cmd中运行）
pip list                      #查看已安装的第三方的包
pip install 包名              #安装第三方的包
pip uninstall 包名            #卸载已安装的包

#做一个“包”：首先创建一个叫做“utils”的文件夹，然后，在里面创建一个叫“_init_.py”的文件，就创建了一个空的包（注意文件的名字是固定的）

#常见的第三方的包
pymysql    #操作MySQL数据库的
selenium
requests
xlrd

#pymysql的使用
import pymysql  #安装好pymsql后，先在“方法集”文件里导入pymsql
pymysql.connect(host="192.144.148.91",user="ljtest",password="123456",db="ljtestdb")  #接下来连接数据库，连接好后，运行一下这条代码，若没有反应，表示来连接成功
db = pymysql.connect(host="192.144.148.91",user="ljtest",password="123456",db="ljtestdb")   #连上之后，把它存到一个变量中，接下来就可以操作数据库了，就可以在数据库里执行sql语句了
#游标  连接上后，还需要个“游标”，也就是命令行中那个一闪一闪地光标，没有游标，就没办法进行操作，所以，接下来就是要获取游标了。这个游标，它也是以一个“方法”的形式体现的
cursor = db.cursor()    #cursor单词的意思就是“游标”，这句代码，也就是取出db里面的游标cursor()，并且把它赋给一个叫做cursor的变量。有了游标之后，就可以运行sql语句了
cursor.execute("show tables;")    #在游标里有个运行sql语句的方法，也就是这句代码，在里面写入sql语句来运行
res = cursor.fetchall()        #运行SQL语句后，我们要获取结果，通过游标cursor里面的fetchall()函数来实现，其中fetchall就表示获取所有结果。获取之后，我们把它存到变量res里
print(res)                #打印出res变量，显示出所获取的结果
db.close()                #然后必须要关闭它，否则会浪费数据库连接的很多资源

#因为SQL语句有很多种，使用的过程中，它是不断变化的，所以，把上述代码做成一个函数/方法，更加方便
def chaxun(sql):       #在上述代码里，前面加上这句代码，把参数改为sql。然后，把cursor.execute("show tables;")的"show tables;"替换为参数sql；然后加上说明就好了（完整的代码，见func文件）

#把sql查询的方法做好后，就可以在别处使用了：
from func import chaxun
chaxun("show tables;")   
chaxun("select * from t_admin;")

#定义一个方法的目的，就是为了能够更方便地使用某个功能，通过调用方法来使得代码更加简洁，不至于把某些代码重复地写很多遍而浪费不必要的时间



def add(a,b):
    """
    目的：是为了计算两个值的和
    """
    c = a + b
    #return 方法返回值
    return c


aa = add(1,2)
print(aa)

#异常处理  try&expect
a = [10,20,30]

try:
    print(a[100])
    print("1")
except:
    print("2")

print("3")

#类  
"""
面向过程：整个工具，方法都一步一步的实现出现   
面向对象：封装成类的方式，来调用

成员变量：类中的变量
普通变量：直接写在py文件或方法里的变量
"""
# 新建一个类：
class Person():
    mingzi = "张三"       # 成员变量：类里面的变量:属性
    shengao = 180
    tizhong = 100
    xingbie = "男"

    #成员方法：类里面的方法
    def pao(self):                               #self为固定用法，sele代表这个类的本身， self存在的目的是，方便方法里面调变量/方法
        print("人可以跑")
        print(self.xingbie)
# 调用类：调用类，专业名词叫做实例化
p = Person()        # Person()实例化Person类，返回类对象并且赋值给p变量  
print(p.mingzi)     # 调用属性
p.pao()             # 调用方法
#print(p.pao())

# 新建一个类：
class Person():
    # 构造方法：实例化类的时候来新建成员变量
    def __init__(self, mz, sg, tz, xb):
        self.mingzi = mz
        self.shenggao = sg
        self.tizhong = tz
        self.xingbie = xb

    # 成员方法：类里面的方法
    # self:固定
    def pao(self):
        print("人可以跑")
        print(self.xingbie)

# 调用类：实例化
p = Person("张三", 180, 100, "女")        # Person()实例化Person类，返回类对象并且赋值给p变量
print(p.mingzi)     # 调用属性
p.pao()             # 调用方法
# print(p.pao())


#类的继承：
class BaBa():
    money = "500W"
    def make_money(self):
        print("爸爸有钱，拿去花！")

class ErZi(BaBa):
    pass                # 占位符号：为了让代码不报错
    

# 子类可以继承父类的属性和方法
ez = ErZi()
print(ez.money)
ez.make_money()



# 重写：子类把父类的属性和方法重新实现
class BaBa():
    money = "500W"
    def make_money(self):
        print("爸爸有钱，拿去花！")

class ErZi(BaBa):
    # pass                # 占位符号：为了让代码不报错
    money = "500E"
    def make_money(self):
        print("儿子终于实现了小目标！")

# 子类把父类的属性和方法重新实现
ez = ErZi()
print(ez.money)
ez.make_money()

