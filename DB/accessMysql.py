import pymysql
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt



# 创建连接

con = pymysql.connect(host="120.78.162.110", port=18330, user="queryUser", \
                      passwd="query@2017", db="bd", charset="utf8")

# 创建游标
cursor = con.cursor()

# 执行sql语句，并返回影响的行数
DTU_ID = 'X18040566'
KEY = "3"


def get_signal(db_cursor, dtu_id, key):
    sql = "SELECT command_content FROM bd.command_log where dtu_id = \'{0}\'\
and command_content like '%\"{1}\":%' order by create_date desc limit 1".format(DTU_ID, KEY)
#    print(sql)
    rownum = db_cursor.execute(sql)
    line = db_cursor.fetchone()
    dic = eval(line[0])
    print(dic)
    signal_val = dic.get(key)
    return int(signal_val)


if __name__ == "__main__":
    signal = get_signal(cursor, DTU_ID, KEY)
    print("dtu_id:{0} signal:{1}".format(DTU_ID, signal))


