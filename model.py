import numpy as np

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
        
