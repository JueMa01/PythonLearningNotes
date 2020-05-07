"""                                   python的判断和循环     """
#if else判断语句，情况更多还要elif
a=1
if a>1:
    print("a大于1")
else:
    print("a小于等于1")
print("好好学习判断")

age=int(input("请输入年龄："))
if age > 60:
    print("耳顺了吗？")
elif age > 30:
    print("而立之年，立起来了吗？")
elif age > 20:
    print("珍惜时间啊，别以为还早着啊！")
else :
    print("加油吧！少年！")

#python的判断符  >  <  ==  !=  in  is  between
name = input("请输入你的名字：")
if name =="张三":
    print("张三！你给我站住！")
else:
    print("啥事儿？")

xx = ["张三","李四","王五","刘六","赵二"]
if name  in  xx:
    print("好兄弟们！")
else:
    print("陌生人！")

if type(name) is str:
    print("输入的是字符串类型")   


b = input("请输入一个整数：")
a = int (b)
if  a>10 and a<50 :             #也可以写成10 < a < 50
    print("在范围内")
else:
    print("在范围外")
#python的逻辑判断连接符  and和or

#练习1：通过input获取账号和密码，如果输入的值满足：账号大于5位并且小于12位，密码是8到16位，那么把账号存到一个字典中，如果条件不满足，请提示原因

#魏林的答案：
a=input("请输入账号：")
b=input("请输入密码：")
c=len(a)
d=len(b)
if 5<c<12 and 8 <= d <= 16:
    x = {
        "user":a,
        "password":b
    }
    print(x)
    print("注册成功！")
elif 5 < c < 12:
    print("密码位数超出规定范围！")
elif 8 <= d <= 16:
    print("账号位数超出规定范围！")
else:
    print("账号和密码的位数超出规定范围！")
#练习1浪老师的答案：
username = input("请输入账号：")
password = input("请输入密码：")
if len(username) > 5 and len(username) < 12:
    if len(password) >= 8 and len(password) <= 16:
        userinfo = {"username":username,"password":password}
        print("注册成功！",userinfo)
    else:
        print("密码不符合规范！")
else:
    print("帐号不符合规范！")

#总结浪老师写的思路：一个条件一个条件的写，分类讨论，由外而内，层层递进!先完成整体框架，再进去完成里面一层，再进一步完成更里面的，直到结束。

#while循环
a = 0
while a < 20:
    print("哈",a)
    a=a+1

#【练习2】：请使用while循环，自动的把数组中下标为单数的值打印出来
xx = [1,2,3,4,"哈哈","嘿嘿","哼哼","啦啦啦","哇咔咔"]

#魏林的答案：
xx = [1,2,3,4,"哈哈","嘿嘿","哼哼","啦啦啦","哇咔咔"]

a = 1
while a <= 8 and a%2 != 0:
    print(xx[a])
    a=a+2

#浪老师的答案：
xx = [1,2,3,4,"哈哈","嘿嘿","哼哼","啦啦啦","哇咔咔"]
a = 1 
while a < len(xx):
    print(xx[a])
    a = a + 2 




#for循环 遍历的方式
#用for循环做练习2
#xx = [1,2,3,4,"哈哈","嘿嘿","哼哼","啦啦啦","哇咔咔"]
a = 1
for i in xx:
    print(xx[a])
    a = a +2

#range() 数列生成器
range(99)                  #range(99) 是省略的写法，表示从0开始，到99结束但又不包含99，不省略的写法就是：range(0,99)
print(range(99))        
print(list(range(99)))   #此处将其转换成数组打印出来了
#range(5,10)                #表示从5开始到10结束，但又不包含10
range(0,10,2)               #表示从0开始，以2位间隔开始递增，到10 结束，但又不包括10（也就是首项为0，公差为2的有限数列，尾项为8）
print(range(0,10,2))        #这种递增的方式也就做“步进”
print(list(range(0,10,2)))   #把这个数列转换成数组的形式打印出来
print(list(range(0,10,3)))   
for i in range(99):
    print(i)

#学了range(),就可以用它来控制循环变量，来完善上面那道用for循环来完成练习2
for i in range(1,len(xx),2):
    print(xx[i])

#【练习3】使用for循环，打印出一个99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i, "x", j, "=",i*j,end = "   ")
    print()

"""
作业1：
现在有10个学生的成绩，需要录入到系统中。
这是个人分别是，张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、朱珠、亚索
并且名字和成绩需要对应上。
而且大于60的和小于60的需要分开存放。
"""
name = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
score = [60,76,88,92,56,59,74,87,99,100]
print(name)
print(score)

#作业2：通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。




name = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
for i in name:
    if i == "小梁":
        continue
    print(i) 

for i in name:
    if i == "小梁":
        break
    print(i)
