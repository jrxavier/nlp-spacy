import spacy
from spacy.symbols import ORTH, LEMMA

nlp = spacy.load('en_core_web_sm')


#NLP Pipelines
#print(nlp.pipe_names)

from spacy import util
print(util.get_package_path('en_core_web_sm'))

doc = nlp(u'I need a taxi to Festy')
for ent in doc.ents:
    print(ent.text, ent.label_)

