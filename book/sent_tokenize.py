#pip install nltk
import nltk
#nltk.download('stopwords')
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords


def sent_token(content):
    sent=[]
    for s in sent_tokenize(content) :
        sent.append(s)

    return sent