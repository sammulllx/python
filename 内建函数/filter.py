# filter(...)
# filter(function or None, sequence) -> list, tuple, or string

# Return those items of sequence for which function(item) is true.  If
# function is None, return the items that are true.  If sequence is a tuple
# or string, return the same type, else return a list.

a = filter(lambda x: x % 2, [1, 2, 3, 4])
print(a)

b = list(a)
print(b)


c = filter(None, "she")
# 'she'
for x in c:
    print(x)


phones = ['18303517744', '15020030417', '15088931331', '15906878938', '13646514938', '13706636314',
          '18867793298', '13739742666', '15731102345', '13859652222', '18232102678', '13601261337',
          '15231099666', '18337728521', '15203802168', '18331758666', '18736599499', '13930109099',
          '15738888289', '15738888538', '15738888576', '15738888697', '15738888963', '13797904444',
          '15243191111', '18405311888', '18405312888', '13791080000', '13791090000',
          '13908376207', '13908335110',
          ]

r = filter(lambda x: x.find('4') == -1, phones)
print(list(r))
