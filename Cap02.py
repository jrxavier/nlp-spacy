import spacy
from spacy.symbols import ORTH, LEMMA

nlp = spacy.load('pt_core_news_sm')



#Tokenization
doc = nlp(u'Eu sou uma pessoa feliz')
print([w.text for w in doc])

#Lemmatization
special_case = [{ORTH:u'Sampa', LEMMA:u'São Paulo'}]
nlp.tokenizer.add_special_case(u'Sampa', special_case)

doc = nlp(u'Estou voando para Sampa')
for token in doc:
    print(token.text, token.lemma_)

#Part-os-speech
doc = nlp(u'Eu viajei para Lisboa. Eu estou viajando para Paris agora')
print([w.text for w in doc if w.tag_== 'VBG' or w.tag_== 'VB' or w.pos_ == 'PROPN'])
#print([w.tag_ for w in doc])

#Named entity recognition
doc = nlp(u'Eu trabalho na CVM mas ano que vem vou para o BNDES')
for token in doc:
    if token.ent_type != 0:
        print(token.text, token.ent_type)

print('########################')
doc = nlp(u'Uma frase é algo interessante quando o nome busca a verdade')
for chunk in doc.noun_chunks:
    print(chunk)

print('########################')
doc = nlp(u'The Golden Bridge é um ícone de San Francisco')
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.dep_)


