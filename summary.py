import spacy
import re
from collections import Counter
import math

nlp=spacy.load("en_core_web_sm")

def summaryText(text):
    text=re.sub(r'\s+', ' ', text)
    doc=nlp(text)
    sentences=[sentence.text for sentence in doc.sents]
    if len(sentences)>4:
        length=0.25*len(sentences)
    else:
        length=0.5*len(sentences)
    length=math.ceil(length)
    freq=Counter()
    for token in doc:
        if not token.is_stop and not token.is_punct:
            freq[token.lemma_.lower()]+=1
            
    maxFreq=max(freq.values())
    for word in freq:
        freq[word]/=maxFreq
    
    sentenceScore={}
    
    for sentence in doc.sents:
        for word in sentence:
            if word.lemma_.lower() in freq:
                sentenceScore[sentence.text]=sentenceScore.get(sentence.text,0)+freq[word.lemma_.lower()]
    
    sortedSentences=sorted(sentenceScore,key=sentenceScore.get,reverse=True)
    sortedSentences=sortedSentences[:length]
    actualOrder=[]
    for sentence in sentences:
        if sentence in sortedSentences:
            actualOrder.append(sentence)
    summary=" ".join(actualOrder)
    return summary
        
    