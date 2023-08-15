import jieba
import numpy as np 
from collections import defaultdict

class Corpus(object):
    def __init__(self, data):
        self.tags = defaultdict(int)
        self.vocabs = set()
        self.docs = []
        
        self.build_vocab(data)
        self.v_l = len(self.vocabs)
        self.d_l = len(self.docs)   
    
    def tokenizer(self, sent):
        return jieba.lcut(sent)

    def build_vocab(self, data):
        for (tag, doc) in data:
            words = self.tokenizer(doc)
            self.vocabs.update(words)
            self.tags[tag] += 1
            self.docs.append((tag, words))
        self.vocabs = list(self.vocabs)
    
    def calc_bow(self):
        self.bow = np.zeros([self.d_l, self.v_l])
        for idx in range(self.d_l):
            for word in self.docs[idx][1]:
                if word in self.vocabs:
                    self.bow[idx, self.vocabs.index(word)] += 1
    
    def calc_tfidf(self):
        self.calc_bow()
        
        self.tf = np.zeros([self.d_l, self.v_l])
        self.idf = np.ones([1, self.v_l])
        self.tf_idf = np.ones([self.d_l, self.v_l])
        for idx in range(self.d_l):
            self.tf[idx] = self.bow[idx] /np.sum(self.bow[idx])
            for word in self.docs[idx]:
                if word in self.vocabs:
                    self.idf[0, self.vocabs.index(word)] += 1
        self.idf = np.log(float(self.d_l) / self.idf)
        self.tfidf = self.tf * self.idf
        
    def get_idx(self, words):
        bow = np.zeros([1, self.v_l])
        for word in words:
            if word in self.vocabs:
                bow[0, self.vocabs.index(word)] += 1
        return bow

class NBayes(Corpus):
    def __init__(self, data, kernel="tfidf"):
        super(NBayes, self).__init__(data)
    
        self.kernel = kernel
        self.y_prob = {}
        self.c_prob = None
        self.feature = None
    
    def train(self):
        if self.kernel == "tfidf":
            self.calc_tfidf()
            self.feature = self.tfidf
        else:
            self.calc_bow()
            self.feature = self.bow
    
        for tag in self.tags:
            self.y_prob[tag] = float(self.tags[tag])/ self.d_l

        self.c_prob = np.zeros([len(self.tags), self.v_l])
        Z = np.zeros([len(self.tags), 1])

        for idx in range(self.d_l):
            tid = list(self.tags.keys()).index(self.docs[idx][0])
            self.c_prob[tid] += self.feature[idx]
            Z[tid] = np.sum(self.c_prob[tid])

        self.c_prob /= Z
    
    def predict(self, inp):
        words = self.tokenizer(inp)
        idx = self.get_idx(words)

        tag, score = None, -1
        for (p_c, y) in zip(self.c_prob, self.y_prob):
            tmp = np.sum(idx * p_c * self.y_prob[y])

            if tmp > score:
                tag = y
                score = tmp
        return tag, 1.0 - score

trainSet = [("pos", "good job !"),
            ("pos", "表現很好"), 
            ("pos", "厲害喔"),  
            ("pos", "做的真好"), 
            ("pos", "很棒"),
            ("pos", "給你按讚"),
            ("neg", "太差了"), 
            ("neg", "真糟糕"), 
            ("neg", "一點都不好"), 
            ("neg", "不行"),
            ("neg", "真慘"),
            ("neg", "真爛"),
			("neg", "很不好"),
            ("neg", "太差勁了"),
            ("neg", "so bad"),
            ("neu", "普普通通吧"), 
			("neu", "都一樣"),
            ("neu", "差不多"),
            ("neu", "不多也不少"),
            ("neu", "剛好而已"),
            ("neu", "同樣啦"),			
			("neu", "看不出來"),
			("neu", "有差嗎"),
			("neu", "so so"),			
            ("neu", "沒變化")
               ]
               
nb = NBayes(trainSet)
nb.train()
print(nb.predict("沒救了"))
print(nb.predict("沒差吧"))
print(nb.predict("值得嘉獎"))