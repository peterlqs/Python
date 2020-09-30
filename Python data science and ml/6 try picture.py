import nltk
nltk.download()
messages = [line.rstrip() for line in open('smsspamcollection/SMSSpamCollection')]
print(len(messages))