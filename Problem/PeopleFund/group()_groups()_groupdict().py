import re

string = input().strip()
m = re.search(r'([a-zA-Z\d])\1+', string)
print(m.group(1) if m else -1)
