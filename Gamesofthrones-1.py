ef gameOfThrones(s):
    #counting frequency of each char
    c = Counter(s)
    # if len of s is even then frequency of each char must be even 
    # to be palindrome and anagram both
    if len(s)%2==0:
        for val in c:
            if c[val]%2!=0:
                return "NO"
    # if len is odd the must be only one char frequency is odd 
    # more than one char having odd frequency would not be a 
    # palindrome + anagram
    else:
        odd = 0
        for val in c:
            if c[val]%2!=0:
                odd += 1
        if odd > 1:
            return "NO"
        else:
            return "YES"
    
    return "YES"     
