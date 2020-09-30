import re
print(re.search(r'cat|dog',"The cat is here"))
print(re.findall(r'..at','The cat in the hat went splat.'))
print(re.findall(r'\d','2 and 10 is a number'))
# ^ is start with , $ is end with
#[^_____} is exclude
print('\n')
phrase = 'there are 3 numbers 34 inside 5 sentence'
pattern = r'[^\d]+'
print(re.findall(pattern,phrase))
print('\n')
text = "Only find the hypen-words in this sentence. But you don't know how long-ish"
pattern = r"[\w]+-[\w]+"    #[] is not necesarry
print(re.findall(pattern,text))

