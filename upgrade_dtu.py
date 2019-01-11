# -*- coding:utf-8 -*-
# !E:\\Project\\Python\\python
import Tools.ProgramBar as Bar
import time
from urllib import request
import pymysql
import DB.accessMysql as condb
# import os
#   ---------------  config start --------------------------------
UPDATE_NAME = "X-DTU_V2.09_4CC47B5A.bin"
UPDATE_TOKEN = "107464fc-0723-47aa-b6e8-7f310ab0dc3b"

DTU_VERSION = "DTU_V2.02"
ONLINE = True

db_config = {
    "host": "120.78.162.110",
    "port": "18330",
    "user": "queryUser",
    "passwd": "query@2017",
    "db": "bd",
    "charset": "utf8"
}

#  ------------------ config end --------------------------------
def query_data():
    test_bar = Bar.ProgressBar(time.perf_counter())

    for i in range(3):
        time.sleep(1)
        test_bar.run_progressbar(i + 1, 3)
    print()
    print("query done")


def upgrade_dtu(dtu_id_list):
    url_array = list()
    for id in dtu_id_list:
        url = "http://bd.qhxwl.com:18443/baod/upgrade/add.shtml?token=" + UPDATE_TOKEN + "&dtu_id="\
        + id + "&file_name=" + UPDATE_NAME + "&file_size=11111111111111&rule=01"
        url_array.append(url)
        print(url)
    upgrade_bar = Bar.ProgressBar(time.perf_counter())
    for i, url_item in enumerate(url_array):
        #    print("url:{0}".format(url_item))
        with request.urlopen(url_item) as f:
            data = f.read()
            #            print("status:", f.status, f.reason)
            #            for k, v in f.getheaders():
            #               print("%s:%s" %(k, v))
            # print("DTU_ID:", id_array[i], end="  ")
            if data.decode("utf-8").find("用户未登录或登录超时") != -1:
                print("token 已失效！")
                break
            # else:
            #     print("命令下发成功")
        upgrade_bar.run_progressbar(i+1, len(url_array))
        time.sleep(20)
    print("\n{0:*^50}\n".format("upgrade done"))


def check_upgrade_result():
    print("check_upgrade_result done")


def exit_process():
    print("exit_process done")


def do_job(index):
    switch = {
        1: query_data,
        2: upgrade_dtu,
        3: check_upgrade_result,
        4: exit_process
    }
    try:
        switch[index]()
    except Exception as err:
        print(err)


def print_info():
    print()
    print("*   +----------------------o00o-(_)-o00o---------------------+   *")
    print("*   |                                                        |   *")
    print("*   | [1].  query db and export dtu_id result                |   *")
    print("*   | [2].  upgrade dtu_id                                   |   *")
    print("*   | [3].  check  upgrade status                            |   *")
    print("*   | [4].  exit                                             |   *")
    print("*   |                                                        |   *")
    print("*   +---------------------- oooO---(   )---------------------+   *")
    print()


def show_menu():
    while True:
        print_info()
        get_str = input("please input the number :")
        select_index = eval(get_str.strip())
        if select_index == 4:
            break
        elif select_index not in range(1, 5):
            print("input error, <usage>: input number ")
        else:
            do_job(select_index)


if __name__ == "__main__":

    # 1.显示程序名称及版本信息
    Bar.show_head_info("DTU Remote Upgrade", "V1.00")

    # 2. 显示用户操操作菜单
    show_menu()

    # 3. 创建连接
    con = pymysql.connect(**db_config)

    # 4. 创建游标
    cursor = con.cursor()

    # 5. select
    condb.selet_verion_data(cursor, DTU_VERSION, ONLINE)
