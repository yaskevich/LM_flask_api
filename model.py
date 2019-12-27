import numpy as np
import pickle
import nltk
import random

class myBert():

    def __init__(self):
        self.words = []

    def get_probabilities(self, sentence):
        self.words = sentence.split(' ')
        scores = np.random.randint(10, size=len(self.words))
        probs  = scores /np.sum(scores)
        sent_probs = { word : probs[indx] for indx, word in enumerate(self.words)}
        result={}
        result['sentence_probs'] = sent_probs
        for head in range(12):
            result['head_#'+str(head)] = np.random.rand(len(self.words),len(self.words)).tolist()
        return result

class myHMM():

    def __init__(self):
        with open('./cprob_nkra', 'rb') as f:
            self.HMM = pickle.load(f)

    def get_words(self, word, count = 10):
        self.clear = str(word).strip()
        d = self.HMM[self.clear].freqdist()
        result = sorted(d.items(), key=lambda x: x[1],reverse=True)[:count]
        if result == []:
            return random.choice(list(self.HMM))
        else:
            result = [{i:j} for i,j in result]
            return result
