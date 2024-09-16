# 计算0到7之间的奇数个数
# count = sum(1 for i in range(8) if i % 2 != 0)

cnt = 0
for x in range(8):
    if x % 2 != 0:
        cnt += 1
print(cnt)  # 输出结果
