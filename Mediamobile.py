def media_mobile(l,n):
    r = []
    for i in range(len(l)):
        if i < n-1:
            r.append(sum(l[:i+1])/(i+1))
        else:
            r.append(sum(l[i-n+1:i+1]) / n)
    return r

lista = [1,2,3,4,5,6,7,8,9,10]
n=3
print(media_mobile(lista, n))




