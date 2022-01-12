from utils import ponctuation_check
from utils import capital_word_check
from utils import clean_data

from utils import embed_sentence_with_TF
import numpy as np
import pickle
from gensim.models import Word2Vec
import gensim.downloader as api
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import models
import re
def create_features(tweet):
    score_punctuation = ponctuation_check(tweet)
    score_capitalization = capital_word_check(tweet)

    return np.array([score_punctuation, score_capitalization])

def create_emojis2text(tweet):
    pass

def tokenize_tweet(tweet):
    tweet_tokenized = clean_data(tweet)
    return tweet_tokenized


def embed_tweet(tweet_tokenized):
    # import w2v trained
   # with open('../project_BAN/models/word2vec_transfer', 'rb') as handle:
   #     word2vec_transfer = pickle.load(handle)
    word2vec_transfer = api.load("glove-twitter-50")

    # embed
    tweet_emebedded = embed_sentence_with_TF(word2vec_transfer, tweet_tokenized)

    #reshape to 3D
    tweet_emebedded = np.array(tweet_emebedded)
    tweet_emebedded_reshape  = tweet_emebedded.reshape((1,tweet_emebedded.shape[0],tweet_emebedded.shape[1]))
    tweet_emebedded_pad = pad_sequences(tweet_emebedded_reshape, dtype='float32', padding='post', maxlen=200)
    return tweet_emebedded_pad
