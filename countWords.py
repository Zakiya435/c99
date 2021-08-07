intro = input("Enter your introduction")
print(intro)

charCount = 0
wordCount = 1

for i in intro:
    if i==' ':
        wordCount+=1
    charCount+=1

print(charCount)
print(wordCount)