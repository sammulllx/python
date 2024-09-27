import time


def calculate_10w():
    '''
    计算10000以内的每个数的立方和
    '''
    sum_ret = 0
    for i in range(1, 100001):
        sum_ret += i ** 3
    print("10w以内每个数的立方和为", sum_ret)


start_time = time.time()
calculate_10w()
stop_time = time.time()

print("总耗费时长为:", stop_time-start_time, "秒")
