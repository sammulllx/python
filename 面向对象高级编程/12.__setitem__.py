class Foo(object):
    def __init__(self, name):
        self.name = name

    def __getitem__(self, key):
        if key == 'name':
            return self.name
        else:
            return 'no find'

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass


f = Foo('sammul')

print(f['name'])
