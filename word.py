str = input()
def checkPalindrome(str):
    return str == str[::-1]
def Comb(str, n):
    if (n == 2):
        comb = {}
        pal = set()
        ij = [(i,j) for i in range(len(str)) for j in range(len(str)) if i < j]
        for (i,j) in ij:
            comb[str[i] + str[j]] = i
            if checkPalindrome(str[i] + str[j]): pal.add(str[i] + str[j])
        return [comb, pal]
    else:
        comb = Comb(str,n-1)[0]
        thisComb = {}
        thisPal = set()
        ij = [(i,piece) for i in range(len(str)) for piece in comb if i < comb[piece]]
        for (i,piece) in ij:
            thisComb[str[i] + piece] = i
            if checkPalindrome(str[i] + piece): thisPal.add(str[i] + piece)
        return [{**comb, **thisComb}, (Comb(str,n-1)[1].union(thisPal))]


print(Comb(str,len(str))[1] if len(Comb(str,len(str))[1]) > 0 else "No palindrome")