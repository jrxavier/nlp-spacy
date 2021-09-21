import spacy
#from spacy.symbols import ORTH, LEMMA

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'The firm earned $1.5 million in 2017, in comparison with $1.2 million in 2012.')

phrase = ''
for token in doc:
    if token.tag_ == '$':
        phrase = token.text
        i = token.i + 1
        while doc[i].tag_ == 'CD':
            phrase += doc[i].text + ' '
            i+= 1
        #break
        phrase = phrase[:-1]
        print(phrase)


doc = nlp(u'I can promise it is worth your time.')
sent = ''
for i, token in enumerate(doc):
    if token.tag_ == 'PRP' and doc[i+1].tag_ == 'MD' and doc[i+2].tag_ == 'VB':
        sent = doc[i+1].text.capitalize() + ' ' + doc[i].text
        sent = sent + ' ' + doc[i+2:].text
        break

doc = nlp(sent)
for i, token in enumerate(doc):
   if token.tag_ == 'PRP' and token.text == 'I':
       sent = doc[:i].text + ' you ' + doc[i+1:].text
       break

doc = nlp(sent)
for i, token in enumerate(doc):
   if token.tag_ == 'PRP$' and token.text == 'your':
       sent = doc[:i].text + ' my ' + doc[i+1:].text
       break

doc = nlp(sent)
for i, token in enumerate(doc):
   if token.tag_ == 'VB':
       sent = doc[:i].text + ' really ' + doc[i:].text
       break

doc = nlp(sent)
sent = doc[:len(doc) -1 ].text + '?'

print(sent) 