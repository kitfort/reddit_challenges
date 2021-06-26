# count 1s in list and ignore 0s
# i.e. [1,0,1,1,0,0,0,0,1,1,1,1,1] = 1, 2, 5

a = [0,0,0,0,0]
b = [1,1,1,1,1]
c = [0,1,1,1,1,1,0,1,1,1,1]
d = [1,1,0,1,0,0,1,1,1,0,0]
e = [0,0,0,0,1,1,0,0,1,0,1,1,1]
f = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

def nonogram(binary_array):
    nonogram_list = []
    one_count = 0
    for element in binary_array:
        if element == 1:
            one_count += 1
        else:
            if one_count > 0:
                nonogram_list.append(one_count)
            one_count = 0
    if one_count > 0:
        nonogram_list.append(one_count)
    print(nonogram_list)


nonogram(a)
nonogram(b)
nonogram(c)
nonogram(d)
nonogram(e)
nonogram(f)
