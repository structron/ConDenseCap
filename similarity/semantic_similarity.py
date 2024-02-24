import spacy
import numpy as np

def sentence_similarity(sent1, sent2):
    '''
    Return the Spacy similarity between two sentences
    inputs:
        sent1: spacy parsed sentence
        sent2: spacy parsed sentence
    '''
    return sent1.similarity(sent2)

def spacy_parse_list(texts, nlp):
    '''
    Return the Spacy parse of a text list
    inputs:
        texts: list of texts
        nlp: spacy nlp object
    '''
    return [nlp(text) for text in texts]

def get_similarity_matrix(docs1, docs2):
    similarities = np.zeros((len(docs1), len(docs2)))
    for i, doc1 in enumerate(docs1):
        for j, doc2 in enumerate(docs2):
            similarities[i, j] = sentence_similarity(doc1, doc2)
    
    return similarities
    