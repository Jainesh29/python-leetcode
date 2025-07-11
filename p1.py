#  This code separates repeating and non-repeating elements in a list.
a = [1,2,3,4,55,6,55]
b = {'repeating': [],'non-repeating': [] }
for i in a:
    if a.count(i) > 1: # Checking if the element appears more than once
        b['repeating'].append(i)
    else:
        b['non-repeating'].append(i)
print(b)