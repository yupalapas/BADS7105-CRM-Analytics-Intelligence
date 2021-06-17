# -*- coding: utf-8 -*-
"""็Homework 11 - Customer Voice Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zs6eJHeiXho1c-ssZlqxcs-VbMPb2x4f
"""

!pip install --upgrade pythainlp
!pip install pyLDAvis
!pip install -U pandas-profiling
!pip install sefr_cut

import pandas as pd
import pythainlp
import sefr_cut
import gensim
# import pyLDAvis.gensim
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
pyLDAvis.enable_notebook()
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

df = pd.read_csv('CustomerReviews.csv')

df.head(5)

"""Tokenize Words"""

stopwords = list(pythainlp.corpus.thai_stopwords())
removed_words = [' ', '  ', '\n','\n\n', 'ร้าน', '(', ')' , '           ','–', '!', '!!','-','/','+','😆','🤣','"','','%','\u200b','::']
screening_words = stopwords + removed_words

sefr_cut.load_model(engine='ws1000')
def tokenize_with_space(sentence):
  merged = ''
  # words = pythainlp.word_tokenize(str(sentence), engine='newmm')
  words = sefr_cut.tokenize(sentence)
  for word in words[0]:
    if word not in screening_words:
      word = word.rstrip("\n")
      word = word.rstrip("\u200b")
      if word is None or word == ' ' or word == '' or word ==':':
        continue
      else: 
        merged = merged + ',' + word
    elif word is None:
      continue
  return merged[1:]
  
  # return words

df['Review_tokenized'] = df['Review'].apply(lambda x: tokenize_with_space(x))

df.info()

df['Review_tokenized'].iloc[10]

df.tail()

"""
Create Dictionary"""

# documents = df['Review_tokenized'].to_list()
documents = df['Review_tokenized']
texts = [[text for text in doc.split(',')] for doc in documents]
dictionary = gensim.corpora.Dictionary(texts)

print(dictionary.token2id.keys())

gensim_corpus = [dictionary.doc2bow(text, allow_update=True) for text in texts]
word_frequencies = [[(dictionary[id], frequence) for id, frequence in couple] for couple in gensim_corpus]

"""Topic Modelling"""

# Commented out IPython magic to ensure Python compatibility.
num_topics = 5
chunksize = 4000 # size of the doc looked at every pass
passes = 20 # number of passes through documents
iterations = 100
eval_every = 1  # Don't evaluate model perplexity, takes too much time.

# Make a index to word dictionary.
temp = dictionary[0]  # This is only to "load" the dictionary.
id2word = dictionary.id2token

# %time model = gensim.models.LdaModel(corpus=gensim_corpus, id2word=id2word, chunksize=chunksize, \
                       alpha='auto', eta='auto', \
                       iterations=iterations, num_topics=num_topics, \
                       passes=passes, eval_every=eval_every)

# pyLDAvis.gensim.prepare(model, gensim_corpus, dictionary)
gensimvis.prepare(model, gensim_corpus, dictionary)

model.show_topic(3)

df['topics'] = df['Review_tokenized'].apply(lambda x: model.get_document_topics(dictionary.doc2bow(x.split(',')))[0][0])
df['score'] = df['Review_tokenized'].apply(lambda x: model.get_document_topics(dictionary.doc2bow(x.split(',')))[0][1])
df['topic_name'] = df['Review_tokenized'].apply(lambda x: model.show_topic(model.get_document_topics(dictionary.doc2bow(x.split(',')))[0][0]))
df['topic_name2'] = df['topic_name'].apply(lambda x:convert_to_topic(x))

df[['Restaurant', 'Review', 'topics','topic_name2','score']]

"""Interpretation

พบว่า Topic Name สามารถแบ่งย่อยได้ 5 เรื่อง 

Topic 0 พูดถึง ดี น้ำ ราคา เนื้อ อาหาร ทาน หวาน อร่อย กิน คุ้ม

Topic 1 พูดถึง กิน ดี เนื้อ คน เลือก ทาน น้ำ ราคา อร่อย บาท

Topic 2 พูดถึง เนื้อ น้ำ ทาน เลือก ซุป อร่อย ดี หวาน กิน

Topic 3 พูดถึง ทาน ดี เนื้อ เลือก ราคา อาหาร น้ำ บาท สาขา อร่อย

Topic 4 พูดถึง กิน ดี อาหาร ทาน คน อร่อย เนื้อ สด น้ำ เลือก



ดังนั้นแต่ละ Topic ควรชื่อว่า

Topic 0 ราคาคุ้ม เนื้อดี อาหารอร่อย 

Topic 1 ราคาดี เนื้ออร่อย

Topic 2 ซุปหวานอร่อย เนื้อดี

Topic 3 เนื้อดี อาหารน้ำคุ้มราคา

Topic 4 เนื้อสด อาหารดี อร่อย เลือกทานได้
"""