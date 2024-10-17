  myiterator = iter(mylist)
    try:
        while True:
            print(next(myiterator))
    except StopIteration as e:
        print(f'Stopped: {e}')