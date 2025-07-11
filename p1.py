a = [1,2,3,4,55,6,55]
b = {'repeating': [],'non-repeating': [] }
for i in a:
    if a.count(i) > 1:
        b['repeating'].append(i)
    else:
        b['non-repeating'].append(i)
print(b)