"""Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

// Constraints:

// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters."""

strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    # dictValue = {}
    # retVal = ""
    # flag = 0
    # minLength = 0
    # if (len(strs) > 0):
    #     print("")
    #     for i in strs:
    #         minLength = len(i) if (len(i) <= minLength or minLength == 0) else minLength
        
                   

    #     print(retVal)
    # else:
    #     print("List is empty")
    #     return 0
    retVal = ""
    minLength = 0      
    strs1 = strs.sort(key = str.lower)
    print(strs1)
    for i in strs:
        minLength = len(i) if (len(i) <= minLength or minLength == 0) else minLength
    if (minLength == 0):
        return ""
    if (minLength <= 1):
        return strs[0]
    for i in range(minLength):
        char =
        if (strs[0][i] == strs[1][i] == strs[2][i]):
            retVal += strs[0][i]
    return retVal

longestCommonPrefix(strs)