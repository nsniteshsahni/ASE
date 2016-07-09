import re
import collections

# Defining list of alphabets for english language
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# A utility function to train your python script about english language
def training(features):
    models = collections.defaultdict(lambda: 1)
    for f in features:
        models[f] += 1
    return models

def words(text): return re.findall('[a-z]+', text.lower()) 

NWORDS = training(words(open('RockYou.txt').read())) # utility file 'RockYou.txt' should be in the same directory as of this code

# to split words
def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

# To compute conditional probability
def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

# a function which can be called via any external file to use this engine
def autosug(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)
