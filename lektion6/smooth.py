def smooth(a):
    res = []
    res.append(a[0])
    for i in range(1, len(a)-1):
        res.append(sum(a[i-1:i+2])/3)
    res.append(a[-1])
    return res

def smooth_a(a, n):
    res = []
    N = len(a) - 1

   # for i in range(0, N):
    #    res.append(sum(a[max(i-n,0):min(i+n,N)])/(2*n +1))

    for i in range(len(a)):
        k = 0
        for j in range(2*n+1):
            k = sum(a[max(i-j,0):min(i+j,N)])

        res.append(k/(2*n+1))

    return res

x = [1, 2, 6, 4, 5, 0, 1, 2]
print('smooth_a(x, 1): ', smooth_a(x, 1))
print('smooth_a(x, 2): ', smooth_a(x, 2))

#smooth_a(x, 1): [1.3333333333333333, 3.0, 4.0, 5.0, 3.0, 2.0, 1.0, 1.6666666666666667] 
#smooth_a(x, 2): [2.2, 2.8, 3.6, 3.4, 3.2, 2.4, 2.0, 1.4]
#smooth_b(x, 1): [1.5, 3.0, 4.0, 5.0, 3.0, 2.0, 1.0, 1.5]
#smooth_b(x, 2): [3.0, 3.25, 3.6, 3.4, 3.2, 2.4, 2.0, 1.0]
