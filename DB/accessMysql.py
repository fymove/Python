import pymysql
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

DTU_ID = 'X18040566'
KEY_SIGNAL = "3"
ONLINE = True
DTU_VERSION = "DTU_V2.02"

db_config = {
    "host": "120.78.162.110",
    "port": 18330,
    "user": "queryUser",
    "passwd": "query@2017",
    "db": "bd",
    "charset": "utf8"
}
# 创建连接

con = pymysql.connect(**db_config)

# 创建游标
cursor = con.cursor()

# 执行sql语句，并返回影响的行数


def get_key_val(db_cursor, dtu_id, key):
    sql = "SELECT command_content FROM bd.command_log where dtu_id = \'{0}\'\
and command_content like '%\"{1}\":%' order by create_date desc limit 1".format(dtu_id, key)
#    print(sql)
    try:
        rownum = db_cursor.execute(sql)
    except Exception as err:
        print(err)

    line = db_cursor.fetchone()
    if not line:
        print("僵尸数据！！dtu_id:{}".format(dtu_id), "\n")
        signal_val = "-1"
    else:
        dic = eval(line[0])
    #    print(dic)
        try:
            signal_val = dic.get(key)
            # print("signal:",signal_val)
        except Exception as err:
            print(err)
            signal_val = "-2"
    return int(signal_val)


def selet_verion_datas(db_cursor, version, key, online=True):
    online_check = "d.is_connected = 1 and " if online else ""
    sql = "SELECT di.dtu_id,di.dtu_softv FROM bd.device_info di\
    join device d on di.dtu_id=d.dtu_id where {0} dtu_softv in(\'{1}\')".format(online_check, version)

    rownum = db_cursor.execute(sql)
    print("\n数据总条数：", rownum, '\n')
    lines = db_cursor.fetchall()
    # print(lines)
    ids = [x[0] for x in lines]

    signal_vals = []
    # print(ids)
    for dtuid in ids:
        signal = get_key_val(db_cursor, dtuid, key)
        signal_vals.append(signal)

    df = pd.DataFrame({"dtu_id": [x[0] for x in lines], "dtu_version": [x[1] for x in lines],\
                       "signals": signal_vals})

 #   print(df)

    # try:
    #     df["signals"].astype(int)
    # except Exception as err:
    #     print("astype:", err)

  #  print(df.dtypes(df["signals"]))
    print("\nstart to sort signals....\n")
    df.sort_values(by="signals", ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    #rint(df)
    print("\n sorted end\n")

    out_file = ".\\\\{0}.xlsx".format(version)
    print( "write to",  out_file)
    df.to_excel(out_file, version)

    return df


def send_update_cmd(db_cursor, dtu_id_list):
    pass


def check_update_status():
    pass


if __name__ == "__main__":
    df = selet_verion_datas(cursor, DTU_VERSION, ONLINE)
    send_update_cmd()
    check_update_status()

