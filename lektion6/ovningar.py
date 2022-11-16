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


l = [3, 1, 8, 19, 2, 5, 12]
print(between(l, 3, 12))        # Skriver [3, 8, 5, 12]

