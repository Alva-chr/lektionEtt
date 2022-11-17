def smooth(a):
    res = []
    res.append(a[0])
    for i in range(1, len(a)-1):
        res.append(sum(a[i-1:i+2])/3)
    res.append(a[-1])
    return res

def smooth_a(a, n):
    res = []
    

