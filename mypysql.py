# 导入pymysql模块
import pymysql
# 连接数据库
# conn = pymysql.connect(host = "pigcms0871.mysql.rds.aliyuncs.com", user = "test", passwd = "OW3d9WMWQQ", database = "lanmao", charset = "utf8")
conn = pymysql.connect(host = "pigcms0871.mysql.rds.aliyuncs.com", user = "lanmao", password = "OW3d9WMWQQ", database = "lanmao", charset = "utf8")
# 得到一个可执行sql语句的光标对象
cursor = conn.cursor()
# 执行sql语句
ret = cursor.execute("select orderNo from t_order where status = 2 and inOutStatus = 1")
cursor.execute("select orderNo from t_order where status = 2 and inOutStatus = 1")
ret2 = cursor.fetchall()
# cursor.execute("select count(orderNo) from t_order where status = 2 and inOutStatus = 1")
# ret2 = cursor.fetchall()
#关闭光标对象
cursor.close()
#关闭连接数据库
conn.close()

for i in range(0, ret):
    print(ret2[i][0])

