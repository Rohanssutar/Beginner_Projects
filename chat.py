slangs = {
    'brb':'be right back',
    'lol':'laughing out loud',
    'idk':"I don't know",
    'ttyl':'Talk to you later',
    'fam':'Close friend',
    'goat':'Greatest of all time',
    'smh':'shaking my head',
    'gg':'good game',
    'ikr':'I know, right?',
    'bet':'Ok or alright',
    'cap':'lie',
    'drip':'Cool style',
    'rizz':'flirting ability',
    'slaps':'is really good'
}

punctuations = "!$%&'()*,.:;?_"
sentence = input().split(" ")

for i in range(len(sentence)):
    word = sentence[i].lower()
    clean_word = ''.join(char for char in word if char not in punctuations)
    if clean_word in slangs:
        punc = word[len(clean_word):]
        sentence[i] = slangs[clean_word] + punc
       
print("\nMeaning:"," ".join(sentence))


