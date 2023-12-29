def func(n, INIT, ARR, iter, w, error):
    for t in range(n - 1):
        for y in range(t, n - t):
            o = ARR[t]
            c = ARR[t + y]
            if abs(o[t]) < abs(c[t]):
                a = o
                o = c
                c = a
            ARR[t] = o
            ARR[t + y] = c
    #BASE CASE
    if iter == 0:
        return INIT
    iter -= 1
    a2 = [0.0] * n
    for j in range(n):
        #GETTING EACH UNKNOW'S ARRAY ("ARR"->the big array'matrix' containing a nb of "arr"->small arrays each unknow equ)
        arr = ARR[j]
        #diff is the part of the equ that will be subtracted (contains the other unkonws past values)
        diff = 0
        l = j + 1
        for p in range(1, n):
            if l >= n:
                l = l - n
            diff += arr[l] * INIT[l]#each past value multiplied with its assigned coefficient
            l += 1
        #THE SOR Rule (Gauss-Seidel is a special case where w=1)
        a2[j] =(1 - w) * INIT[j] + (w / arr[j]) * (arr[n] - diff)
        #Calculating the unknow's approximate error
        error[j] = abs((INIT[j] - a2[j]) / a2[j] * 100)
    INIT = a2
    return func(n, INIT, ARR, iter, w, error)

def LINEAR(n, ARR, INIT, iter, w, a):
    #///////////////////RE-ARRANGE THE MATRIX//////////DIAGONNALLY DOMINANT////////////////
    for t in range(n - 1):
        for y in range(t, n - t):
            o = ARR[t]
            c = ARR[t + y]
            if abs(o[t]) < abs(c[t]):
                a = o
                o = c
                c = a
            ARR[t] = o
            ARR[t + y] = c
    IN=[0.0]*n
    IN = func(n, INIT, ARR, iter, w, a)

    #//get max error//Need to check with Dr Amany which error (all of them or just MAX)
    # THIS PART IS TO BE ADDED IN MAIN IF THE ERROR IS MAX
    #MAXerror = a[0]
    #for h in range(1, n):
    #    if a[h] > MAXerror:
    #        MAXerror = a[h]
    return IN