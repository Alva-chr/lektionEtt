def smooth_a(a, n):
    res = []
    len_a = len(a)
    a = [a[0] for i in range(n)] + a + [a[-1] for i in range(n)]

    for i in range(n, len_a+n):
        x = a[i-n:i+n+1]
        res.append(sum(x)/len(x))

    return res

def smooth_b(a, n):
    res = []

    for i in range(len(a)):
        b = a[max(i-n,0):min(i+n+1,len(a))]
        res.append(sum(b)/len(b))

    return res

def round_list(a_list, ndigits):
    return [round(i, ndigits) for i in a_list]


x = [1, 2, 6, 4, 5, 0, 1, 2]
print('smooth_a(x, 1): ', smooth_a(x, 1))
print('smooth_a(x, 2): ', smooth_a(x, 2))
print('smooth_b(x, 1): ', smooth_b(x, 1))
print('smooth_b(x, 2): ', smooth_b(x, 2))

#smooth_a(x, 1): [1.3333333333333333, 3.0, 4.0, 5.0, 3.0, 2.0, 1.0, 1.6666666666666667] 
#smooth_a(x, 2): [2.2, 2.8, 3.6, 3.4, 3.2, 2.4, 2.0, 1.4]
#smooth_b(x, 1): [1.5, 3.0, 4.0, 5.0, 3.0, 2.0, 1.0, 1.5]
#smooth_b(x, 2): [3.0, 3.25, 3.6, 3.4, 3.2, 2.4, 2.0, 1.0]
