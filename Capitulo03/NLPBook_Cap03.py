import spacy
#from spacy.symbols import ORTH, LEMMA

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'The firm earned $1.5 million in 2017.')

for token in doc:
    print(token.text, token.pos_, token.tag_, spacy.explain(token.tag_))


