def make_pencil(color):
    def write(content):
        print("正在使用(%s)色，写：%s" % (color, content))

    return write


black_pencil = make_pencil("黑")
black_pencil("我是喝墨水长大的")

red_pencil = make_pencil("红")
red_pencil("这么巧，我也是，只不过是红墨水")
