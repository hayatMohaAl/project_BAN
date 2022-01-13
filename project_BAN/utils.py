from tensorflow.keras.preprocessing.text import text_to_word_sequence
from nltk.corpus import stopwords
import numpy as np
import re




def ponctuation_check(tweet):
    score = 0
    for word in tweet.split():
        if word.count('!!!!!') >= 1:
            score += 1
    return score


def capital_word_check(tweet):
    score = 0
    for word in tweet.split():
        if word.isupper():
            score += 1
    return score

def clean_data(data):

    #Removing URLs with a regular expression
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    data = url_pattern.sub(r'', data)

    # Remove Emails
    data = re.sub('\S*@\S*\s?', '', data)

    # tokenize + remove scpecial characters + set to lower case
    data = text_to_word_sequence(data)


    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    data = [w for w in data if not w in stop_words]

    # Remove digits
    data = ' '.join(word for word in data if not word.isdigit())


    return text_to_word_sequence(data)


# Function to convert a sentence (list of words) into a matrix representing the words in the embedding space
def embed_sentence_with_TF(word2vec, sentence):
    embedded_sentence = []
    for word in sentence:
        if word in word2vec:
            embedded_sentence.append(word2vec[word])

    return np.array(embedded_sentence)
