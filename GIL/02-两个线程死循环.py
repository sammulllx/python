import threading


def test():
    while True:
        print('儿子')


t1 = threading.Thread(target=test)
t1.start()

while True:
    print('爸爸')
