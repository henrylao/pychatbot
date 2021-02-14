from typing import List

import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np


# TODO consider usage of static decorator

class Preprocessor(WordNetLemmatizer):
    """ """

    def __init__(self):
        # TODO implement this method
        pass
    # @staticmethod
    def lemmatized(self, sentence) -> List[str]:
        """

        :param sentence:
        :return:
        """
        # TODO rename this method, create docuemntation, assesss parameters
        # tokenize the pattern - splitting words into array
        sentence_words = nltk.word_tokenize(sentence)
        print(len(sentence_words))
        # stemming every word - reducing to base form
        sentence_words = [self.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    # @staticmethod
    def create_bag_of_words(self, sentence, words, show_details=True):
        """

        :param sentence:
        :param words:
        :param show_details:
        :return:
        """
        # TODO rename this method, create docuemntation, assesss parameters
        """  return bag of words array: 0 or 1 for words that exist in sentence """
        # tokenizing patterns
        sentence_words = self.lemmatize(sentence)
        # bag of words - vocabulary matrix
        bag = [0] * len(words)
        for s in sentence_words:
            for i, word in enumerate(words):
                if word == s:
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % word)
        return (np.array(bag))
