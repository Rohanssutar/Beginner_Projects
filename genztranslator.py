import re

slang_dict = {
    "brb":"be right back",
    "lol":"laughing out loud",
    "idk":"I don't know",
    "ttyl":"Talk to you later",
    "fam":"Close friend",
    "goat":"Greatest of all time",
    "smh":"shaking my head",
    "gg":"good game",
    "ikr":"I know, right?",
    "bet":"Okay / deal",

    "cap":"lie",
    "capping":"lying",
    "no cap":"true",

    "drip":"cool style",
    "drippy":"stylish",

    "rizz":"charisma / flirting skills",
    "unspoken rizz":"natural charm",

    "slaps":"is really good",

    "sus":"suspicious",
    "sussy":"suspicious",
    
    "fr":"for real",
    "frfr":"for real, for real",

    "lowkey":"slightly or secretly",
    "highkey":"very or obviously",

    "tea":"gossip or news",
    "spill":"expose / reveal",
    "spilling":"revealing gossip",

    "flex":"show off",
    "flexing":"showing off",

    "simp":"overly affectionate person",
    "simping":"acting overly affectionate",

    "fire":"awesome",
    "lit":"fun",

    "extra":"dramatic",
    "snatched":"looking great",
    "boujee":"luxurious or fancy",
    "bussin":"really good (esp. food)",

    "fomo":"fear of missing out",
    "jomo":"joy of missing out",
    
    "pressed":"angry",
    "stan":"overly enthusiastic fan",
    "receipts":"proof",
    "cheugy":"out of style / trying too hard",

    "vibe":"feeling",
    "vibes":"mood",
    "vibing":"enjoying the mood",
    
    "yeet":"throw / excitement",
    "yeeted":"thrown",

    "ratio":"outnumbered / disproven",
    "woke":"socially aware",

    "ghosted":"ignored / cut contact",
    "ghost":"suddenly cut contact",
    "ghosting":"ignoring / cutting contact",

    "ship":"support a relationship",
    "shipping":"supporting a relationship",

    "glow up":"transformation",
}

words = input("Enter a sentence: ")

for slang in sorted(slang_dict, key=len, reverse=True):
    pattern = r'\b' + re.escape(slang) + r'\b'
    words = re.sub(pattern, slang_dict[slang], words, flags=re.IGNORECASE)
       
print("\nMeaning:", words)