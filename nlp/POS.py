"""
Part of Speech Detection using NLTK library
"""

import nltk
import re
from nltk import pos_tag
from collections import defaultdict
import spacy

# first tkenize the words into individual tokens

# very famous and heart touching words originating from japan

word = """
The broken piece of works an accidentally-smashed pot should never just be tossed away, they should be carefully picked up,
 reassembled and then flued together with lacquer inflected with a luxuriant gold po    wder.There should be no attempt to disguise the damage.
  The point is to render the fault lines beautiful and strong.The precious gold fault is there to emphasise that breaks have a rich merit all of their own.
  It is profoundly poignant idea because we are all in some way broken creature. Its not shameful to need to repair,
   a mended bowl is a symbol of hope that we too can be put together again and again, we could be broken so bad to never to stand again but tomarrow
    we may stand up and dance,and still be loved despite our many obedient flaws.
    """


def word_tokenize(word):
    word = re.compile(r'[^A-Za-z]+').split(word.strip())
    word = filter(None, word)
    return list(word)


def create_dict(tagged):
    """
        this function create the dictionary of tagged words
    """
    tags_lookup = defaultdict(lambda: list())

    for token, tags in tagged:
        tags_lookup[tags] += [token]
    
    return tags_lookup


# to pass the word to pos tagger we need to tokenize the words
tokens = word_tokenize(word)

# Now tag the word with nltk default pos tagger 
tagged = pos_tag(tokens)

# lets create dict from list of tuples which will look preety and follow python standered
tags_lookup = create_dict(tagged)

print('Part of Speech tagging with NLTK default Tagger')
print('-----------------------------------------')
print(tags_lookup)

# Now using spacy to generate pos tags of the sentence 

nlp = spacy.load('en_core_web_sm')
doc = nlp(word)

tagged = [(token.text, token.pos_) for token in doc]

tags_lookup = create_dict(tagged)

print('Part of Speech tagging with spacy default Tagger')
print('-----------------------------------------')
print(tags_lookup)