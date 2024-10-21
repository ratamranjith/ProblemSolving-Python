import re
strings = """Micron Technology, Inc. and its subsidiaries are collectively referred to herein as "Micron." Micron's websites (herein, the “Micron Website(s)” or “Micron’s Website(s)”) are controlled and operated by Micron from its offices in the United States of America. These Terms of Use apply to all of the Micron Websites and all materials and content posted thereon, including but not limited to, text, images, embedded hyperlinks, downloadable content, datasheets, product support documents, and software (collectively referred to herein as “Content”). The Micron Websites are provided on an as-is, where-is basis and Micron provides no representations or warranties as to the accuracy, completeness, or utility of any Content provided on the Micron Websites. Additionally, Micron makes no representations or warranties that the Content contained on Micron's Websites is appropriate or available for use in all locations or territories, and access to such Content from locations or territories where such Content is illegal is prohibited. Failure by Micron to enforce any right(s) or provision(s) contained within these Terms of Use shall not constitute or be deemed to be a waiver of such right(s) or provision(s) nor prevent enforcement by Micron of such right(s) or provision(s) thereafter. Any claim relating to Micron's Websites shall be governed by the laws of the State of Idaho without regard to its"""

strings = (re.sub(r'^[a-zA-Z0-9]+', ' ', strings)).lower().split(" ")

visited = []
newValue = {}
large = 0
for i in strings:
    if i not in visited:
        visited.append(i)
    else:
        large = strings.count(i) if strings.count(i) > large else large
        newValue[i] = strings.count(i)

        
print(visited)
print(newValue)
print(large)