# -*- coding:utf-8 -*-
# !E:\\Project\\Python\\python
import Tools.ProgramBar as Bar
import time
# import os


def query_data():
    test_bar = Bar.ProgressBar(time.perf_counter())
    for i in range(3):
        time.sleep(1)
        test_bar.run_progressbar(i + 1, 3)
    print()
    print("query done")


def upgrade_dtu():
    print("upgrade dtu")


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


Bar.show_head_info("DTU Remote Upgrade", "V1.00")
show_menu()
