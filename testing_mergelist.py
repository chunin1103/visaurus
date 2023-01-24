list1 = ['a dua', 'a qua dang', 'a kich', 'a nong long']
list2 = ['a dua', 'abc', 'def', 'a kich', 'rfcder']

print(list1)
for i in list2:
    if i not in list1:
        list1.append(i)

print(list1)
