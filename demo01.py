"""                                python的常用方法和数据类型"""
#打印函数，括号里是打印的内容。要注意，这些数据内容是有类型的。
print("hello world!")                         #字符串
print("你好!",end="|")                        #其中end="|"表示以end结尾而且不换行，但这是对下一个print函数而言的
print(2333)                                   #整数
print(2.333)                                  #小数
print(True)                                   #布尔值  用来判断对错  TRUE or False
print(None)                                   #空
print(())                                     #元组
print([])                                     #数组
print({})                                     #字典
print("嘻嘻","哈哈","啦啦啦")                  #连续多个打印，逗号隔开

print(((1+3*2)/2)*4)                          #数学运算
print("嘻嘻"+"哈哈")                           #字符串的拼接
print("哈"*10)                                #加倍打印
print(3%2)                                    #求余
print(10%3)
        
#画房子
print( "                       ")
print( "              .   .    ")
print( "             .   .  .  ")
print( "           .     .   . ")
print("         .  ..........  ")
print("         .   ..    ..   ")
print("         .           .  ")
print("         . ...........  ")
"""
#----------------------------------------------------------------------------
"""
#输入函数
input()
input("请输入：")

#变量和赋值
a=1                                       #把1这个值赋给变量a

a=input("请输入：")
print(a)

#练习：通过input分别获取两个值，然后打印出它们相加的结果
#错误答案：
a=input("请输入：")
b=input("请输入：")
print(a+b)

#因为input函数的类型是字符串类型。这一点可以用type函数来检验
print("a的类型是",type(a))                   
print("a+b的类型是",type(a+b))

#数据类型的转换
c=float("1.23")             #字符串转换成了小数
print("c的类型是：",type(c))

#所以上述的练习，其中之一的答案可以是下面这样。转换的思路，有很多，可以在第一二行转换，也可以在第三行转换，还可以另起两行单独给a和b转换
a=input("请输入：")
b=input("请输入：")
print("相加的结果是：",int(a)+int(b))   #要注意，print("相加的结果是：",int(a+b))，这个的意思是，先拼接再转换，输出的虽然是int类型，但形式上还是“拼接”的效果

#数据类型转换的规律： 1 任何数据都可以转换成字符串
                    2 字符串要转换成数字，需要满足长得像的规律
                    3 字符串可以转换成元组、数组

#计算长度的len()函数  注，len()函数，一般字符串可以用，元组、数组、字典可以用，其他的不能用。另外，len()为int型
a=len("dhififhfw")
print(a)

#练习2：通过input分别输入两段字符串，然后获取它们的长度，并相加输出结果
a=input("请输入：")
b=input("请输入：")
print(len(a))           #因为input是str型，而len是int型，所以，在这一步，就把a转换成了int型，下面同理
print(len(b))
print(len(a+b))

#布尔值，用来判断真假条件的   其结果有True和False两种
print(2>1)

#元组  a=()  它是可以用来装东西的，不同的内容用逗号隔开
a=(1,2,3,"哈哈哈","嘻嘻嘻",True)   #元组
print(a)

#下标   如果只是想要打印元组中的某一个值，就要用到下标来标明。这个下标，起始是从0开始算的
a=(1,2,3,"哈哈哈","嘻嘻嘻",True)   #元组
print(a[3])                       #打印元组a中下标为3的值   其中，a[3]这种写法的格式是固定的

#count()统计；index()查询下标
print(a.count(1))                #count统计该内容的个数。注意，True为1，False为0
print(a.index("哈哈哈"))          #查出内容所在的下标
b=(1,2,3,4,a)                     #二维元组 （元组嵌套元组） 注，这里例子中，里面只有五个值
print(b[4][3])                    #表示取出元组b中的元组a中的“哈哈哈”

#数组/列表 list  比如，zz=[]       
zz = [1,2,3,4,5,"haha","哈哈","嘻嘻","呵呵","哼哼","呵呵"，"哼哼"]
print(zz.count("呵呵"))
print(zz.index("哈哈"))

#元组和数组的区别：元组和数组功能基本是一样的，但还是有区别的，元组定义后不可以修改，数组是可以修改的
zz.append("append")          #往数组的尾部追加数据  这个操作就不能针对元组
zz.insert(4,"insert")        #在数组的指定位置插入数据  其中的数字代表想插入的数据的下标
zz.remove("哼哼")             #删除数组中的第一个”哼哼“
zz.pop(5)                    #把下标为5的值取出来
zz[0]=111                    #表示替换，把数组zz中下标为0的内容替换为111（有点相当于赋值）
zz.reverse()                 #把数组zz的内容颠倒

qq = [566,45,1,795,55,36,45,23,29]
qq = ["d","y","p"]
qq.sort（）                   #把数组中的值排序   
qq.sort(reverse=True)         #把数组中的值逆序排序
zz.extend([1,2,3,4,5])       #把一个数组追加到另一个尾巴上，合并起来 （功能和apend相似）
#zz.clear()                   #把数组清空
print(zz)


#通过input分别输入多段字符串，然后获取他们的长度，并且把长度的值分别存放到数组中，并从小到大的排序。
a=input("请输入：")
b=input("请输入：")
c=input("请输入：")
d=input("请输入：")
e=input("请输入：")
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
x=[len(a),len(b),len(c),len(d),len(e)]
x.sort()
print(x)

#---------------------------------------------------------------------------

#字典 键值对 key:value  没有下标，里面的值没有顺序
a={
"name":"李四",
"age":23,
"sex":"男"
}
print(a)
print(a["name"])            #没有下标，通过key来取值

#字典里常用的的方法
a.pop()
a.clear()
a.get()
a.update()
print(a.values())

#往字典里新增数据/修改数据
a.update(name="王五")          #注意：1 update的用法，这里有点特殊，把key当成了一个变量，把“王五”这个值赋给了name，即就是所谓的“更新”
a.update(xxx="哈哈")            #注意：2 如果key值在字典里不存在，就是所谓的“新增”
print(a)

#另一种新增/修改字典数据的方法    （上述写法容易用混淆，所以推荐用这种，这种用法和上述在功能时是一样的）
a["name"]= "张三"
a["xxx"] = "王五"

#取值   下面这三种都是取值，效果一样  但要注意，pop会把字典里的值取出来拿走，字典里就不再有了
print(a["name"])
print(a.get("name"))
print(a.pop("name"))

print(a.keys())        #注意被pop取走后就没有相应的那个key了
print(a.values())
print(list(a.keys()))    #还可以把字典的key和Values转换成数组，下同
print(list(a.values()))

#a.get()和a[]两种取值的区别
print(a.get("name"))  #如果key不存在，那么返回空
print(a["name"])      #如果key不存在，那么报错


#关于往字典里新增的这两种方法，如果key是数字，若有update会报错，若用类似去数组的方法，会成狗往字典里新增数据
b={}
#b.update(1=123)
b[1]=1234
print(b)

