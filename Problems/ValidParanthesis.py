from pympler.tracker import SummaryTracker
tracker = SummaryTracker()

def isValid(s: str) -> bool:
    predefined = { "(" : -1,")" : 1,"{" : -2,"}" : 2,"[" : -3,"]" : 3}
    count = 0
    counter = 0
    for i in s:
        count = count + predefined[i]
        counter += 1
        retVal = False if (count < 0 or counter%2 == 1) else True
    return (True if count == 0 and retVal == True else False)


str = ["()", "()[]{}", "(]", "([)]", "{[]}"]
for s in str:
    print(isValid(s))


tracker.print_diff()