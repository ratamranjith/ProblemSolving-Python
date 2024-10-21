import re

s = "AfterNooN"
pattern = r'(.)(.)(?:(.)\3?\2|\2?)\1'
match = re.match(pattern, s, re.I)

print(match)
