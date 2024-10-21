s = "aaa"
def lengthOfLongestSubstring( s: str) -> int:
        arrayVal = {}
        count = 0
        retVal = 0
        if(len(s) == 0):
            return 0
        for i in s:
            if(arrayVal.get(i, None) == None):
                print(i)
                count += 1
                arrayVal[i] = count
                count = 0
                retVal = len(arrayVal.keys())
            else:
                print(arrayVal.keys())
                arrayVal = {}
                print("---------------------")
                
        return retVal

print(lengthOfLongestSubstring(s))