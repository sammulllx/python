def fibonacci_sequence(n):
    fibonacci_list = [0, 1]
    for i in range(2, n):
        next_num = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_num)
    return fibonacci_list

n = int(input("请输入一个整数 n："))
fibonacci_list = fibonacci_sequence(n)
print("斐波那契数列的前{n}项为:",fibonacci_list)
