def mean(lst):
    return sum(lst)/len(lst)

def median(lst):
    lst_sorted = sorted(lst)
    length = len(lst_sorted)
    return lst_sorted[length//2]

def between(lst, low, high):
    result = []
    for x in lst:
        if low <= x <= high:      # OK att skriva så!
            result.append(x)
    return result

def smoothlol(a):
    lst = []
    lst.append[a[0]]
    
    for i in range(1, len(a)-1):
        lst.append((lst[i] + lst[i+1] + lst[i-1])/3)
    
    lst.append(a[-1])
    return lst

def smooth(a):
    res = []
    res.append(a[0])
    for i in range(1, len(a)-1):
        res.append(sum(a[i-1:i+2])/3)
    res.append(a[-1])
    return res

def counter2(x, lst):
    count = 0
    for lst_level_2 in lst:
        count += lst_level_2.count(x)
    return count

def counter(x, lst):
    count = 0

    for i in lst:

        if type(i) == list:
            count +=  i.count(x)

        elif i == x:
            count += 1

    return count

def extend(lst, x):
    for element in x:
        lst.append(element)

    return lst

def remove_all(lst,x):
    for element in lst:
        if element == x:
            lst.remove(element)

    return lst

lst = [2,3,1,55,67,2,2,1,4,1,2]

print(remove_all(lst, 2))

#lst = ['a', 'b', 'c']

#lst.append([1, 2])
#lst.extend([1, 2])
#print(lst)


#print(counter(1, [[[1, 1]], [1, 2, 1], 1, [1, 2], 1]))        

