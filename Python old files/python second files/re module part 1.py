text = "The agent's phone number is 400-555-1234. Call soon!"
import re
pattern = 'phone'
match = re.search(pattern,text)
text = 'beautiful apple phone and android phone'
matches = re.findall(pattern,text)
print(matches)
for a in re.finditer(pattern,text):
    print(match.group())
