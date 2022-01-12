from utils import ponctuation_check
from utils import capital_word_check
from utils import clean_data

from utils import embed_sentence_with_TF
import numpy as np
import pickle

from tensorflow.keras.preprocessing.text import text_to_word_sequence
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import Sequential, layers
from tensorflow.keras import models

from nltk.corpus import stopwords
import numpy as np
import re

from prep_data import create_features,  tokenize_tweet, embed_tweet



def predict_tweet_class(tweet):
    # prep tweet
    X_features = create_features(tweet)
    tweet_tokenized = tokenize_tweet(tweet)
    tweet_emebedded = embed_tweet(tweet_tokenized)


    # load model
    model = models.load_model('models/model')
    res = model.predict(tweet_emebedded)

    # print text
    if res[0][0]< 0.5:
      text_to_print = "good tweet"
    else:
      text_to_print = "hate tweet"

    return text_to_print

## questions
# how to check right version of libraries en requirements
# __main__ line to add in the end of each *.py
# make?
# are the *.py files in the right path
