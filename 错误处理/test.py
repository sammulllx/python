# def func():
#     raise ValueError("This is a test error")
#     print("This line will not be executed")


# func()
# print("This line will be executed")
# 另外，因为异常没有被捕获，程序会终止，所以 print("This line will be executed") 也不会执行。

def func():
    raise ValueError("This is a test error")
    print("This line will not be executed")


try:
    func()
except ValueError as e:
    print(f"Caught an error: {e}")

print("This line will be executed")

# def func():
#     raise ValueError("This is a test error")
#     print("This line will not be executed")


# for _ in range(3):
#     func()
# print("This line will be executed")
