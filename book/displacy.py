import spacy
nlp = spacy.load('en_core_web_lg')
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
from phruzz_matcher.phrase_matcher import PhruzzMatcher
from spacy.language import Language
from spacy import displacy


#خاص بالأهداف الخاصة بالكمبيوتر
keywords2 = open('media\keywords.txt' ,'r', encoding = 'utf-8')
s1 = " ".join([i for i in keywords2])
phrases_keyword=[]
for i in s1.split('\n '):
    phrases_keyword.append(i)

#---------------------------
@Language.factory("phrasse_matcher")
def phrase_matcher(nlp: Language, name: str):
    return PhruzzMatcher(nlp, phrases_keyword, ".", 85)

nlp = spacy.blank("en")
nlp.add_pipe("phrasse_matcher")

def dis(content):
    doc = nlp(content)
    c = displacy.render(doc , style="ent")
    return c

