import re
s=input()
pattern='[+]91-[6-9]\d{9}'
print(re.findall(pattern,s))

