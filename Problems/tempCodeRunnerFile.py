    retVal = ""
    minLength = 0      
    strs = strs.sort()
    for i in strs:
        minLength = len(i) if (len(i) <= minLength or minLength == 0) else minLength
    if (minLength == 0):
        return ""
    if (minLength <= 1):
        return strs[0]
    for i in range(minLength):
        if (strs[0][i] == strs[1][i] == strs[2][i]):
            retVal += strs[0][i]
    return retVal