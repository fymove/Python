import time

__author__ = "fengyang"
__time__ = 2018/12/26

g_startime = 0
SYMBOL_NUM = 50


class ProgressBar (object):
    def __init__(self, start_time):
        self.start_time = start_time

    def run_progressbar(self, cur_val, total_val):
        time_pass = time.perf_counter() - self.start_time
        real_val = cur_val / total_val * SYMBOL_NUM
        passed = "#" * int(real_val)
        percent = real_val / SYMBOL_NUM * 100
        continued = "." * int(SYMBOL_NUM-real_val)
        print("\rProgress: [{0}{1}]  {2:<.1f}%  {3:.1f}s".format(passed, continued, percent, time_pass), end="")


def test():
    bar = ProgressBar(time.perf_counter())
    for i in range(13):
        time.sleep(1)
        bar.run_progressbar(i+1, 13)


if __name__ == "__main__":
    test()