import numpy as np

def ndot(arr,N):
    if len(arr) == 1 and N == arr[0]:
        return str(N)
    elif len(arr) == 1 and N != arr[0]:
        return False
    for i in set(arr):
        arrTmp = arr[:]
        arrTmp.remove(i)

        c = ndot(arrTmp,N-i)
        if c != False:
            return c + ' + '+str(i)

        c = ndot(arrTmp,N+i)
        if c != False:
            return c + ' - '+str(i)

        c = ndot(arrTmp, N*i)
        if c != False:
            if len(c.split(' '))>1 and c.split(' ')[-2] in '-+':
                return '('+c + ') / ' + str(i)
            else:
                return c + ' / ' + str(i)

        if N%i == 0:
            c = ndot(arrTmp, N // i)
            if c != False:
                if len(c.split(' '))>1 and c.split(' ')[-2] in '-+':
                    return '(' + c + ') * ' + str(i)
                else:
                    return c + ' * ' + str(i)

    return False

alist = list(np.random.randint(1,20,4))

str24 = ndot(alist,24)
print(alist)
print(str24)

# import scipy.io as sio
#
# matFile = '/home/xinxin/下载/vowels.mat'
# data = sio.loadmat(matFile)
#
# feat = data['X']
# label = data['y'].ravel()
#
# import numpy as np
# a = np.array([22,34,5,5,3,4])
#
#
# print(label.shape,feat.shape)
# print(set(label))
# print(feat[:3,:])



