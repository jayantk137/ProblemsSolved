def pickingNumbers(a):
    # Write your code here
    maxi = -1
    for ele in a:
        c = a.count(ele)
        d = a.count(ele-1)
        s =  c+d
        if s>maxi:
            maxi = s

    return maxi     
