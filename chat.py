abbr = {
    'brb':'be right back',
    'lol':'laughing out loud',
    'idk':"I don't know",
    'ttyl':'Talk to you later',
    'fam':'Close friend',
    'goat':'Greatest of all time',
    'smh':'shaking my head',
    'gg':'good game',
    'ikr':'I know, right?'
}

punctuations = "!$%&'()*,.:;?_"
sentence = input().split(" ")

for i in range(len(sentence)):
    word = sentence[i].lower()
    clean_word = ''.join(char for char in word if char not in punctuations)
    if clean_word in abbr:
        punc = word[len(clean_word):]
        sentence[i] = abbr[clean_word] + punc
       
print()
print("Output:"," ".join(sentence))


