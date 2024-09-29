a = {
    'name': 'sam',
    'age': 18
}
b = dict(name='bob', age=19, cars=[100, 200, 1000])

c = b.copy()

print(b)
print(c)

print(id(b))
print(id(c))

b['name'] = 'li'
b['cars'].append(10)

print(b)
print(c)
