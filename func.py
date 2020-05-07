import pymysql

def jiafa(a,b):
    """
    这个方法是实现一个输入任意一个两位的数字，输出他们的和的作用
    """
   
    print(a+b)

def chaxun(sql):
    """
    数据库的查询
    """
    db = pymysql.connect(host="192.144.148.91",user="ljtest",password="123456",db="ljtestdb")
    #游标
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
    db.close()

def add(a,b):
    """
    目的：是为了计算两个值的和
    """
    c = a + b
    #return 方法返回值
    return c


