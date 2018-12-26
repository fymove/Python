import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# 创建连接

con = pymysql.connect(host="120.78.162.110", port=18330, user="queryUser", \
                      passwd="query@2017", db="bd", charset="utf8")

# 创建游标
cursor = con.cursor()

# 执行sql语句，并返回影响的行数
rownum = cursor.execute("SELECT command_content FROM bd.command_log where dtu_id = 'X18040563'\
and command_content like '%\"3\":%' order by create_date desc limit 3")
#alldata = cursor.fetchall()
onedata = cursor.fetchone()
print(onedata[0])
print(type(onedata[0]))
dic = dict(eval(onedata))

#print(dic.get("3"))
print(onedata)

"""

print("总行数为：{}".format(rownum))
for data in alldata:
    print(data)
"""

