import json
import random
import nltk

from server import utils
import pickle
import numpy as np
from keras.models import load_model

ROOT_DIR = utils.get_project_root()
CACHE_DIR = ROOT_DIR / "model_cache"
INPUT_DIR = ROOT_DIR / "input"
print(__name__,"loading from...")
print("Root:", ROOT_DIR)
print("Cache:", CACHE_DIR)
print("Input:", INPUT_DIR)

class ChatBot(nltk.WordNetLemmatizer):
    """ This is the class that encapsulates the loaded NLP trained model 
    and its configurations. 

    """

    def __init__(self, filepaths: dict = None, dataset_name = None):
        # most recent response
        self.label_probability = None
        self.output_message = None
        self.input_message = None
        # model's dataset origin
        self.dataset_name = dataset_name
        self.labels = None
        self.model = None
        self.words = None
        self.intents = None
        # data filepaths
        self._intent_path = None
        self._model_path = None
        self._words_path = None
        self._labels_path = None
        self._version = None
        pass

    def load(self, filepaths: dict = None):
        """
        This is function for loading a model and its related assets
        for launching the bot. The internal function for loading is
        called if there is no configuration of filepaths to be loaded from.

        :param filepaths:
        :return:
        """

        def _load_default():
            self._intent_path = INPUT_DIR / 'dzone-intents.json'
            self._model_path = CACHE_DIR / 'chatbot_model.h5'
            self._words_path = CACHE_DIR / 'words.pkl'
            self._labels_path = CACHE_DIR / 'classes.pkl'
            self.intents = json.loads(open(self._intent_path).read())
            self.model = load_model(self._model_path)
            self.words = pickle.load(open(self._words_path, 'rb'))
            self.labels = pickle.load(open(self._labels_path, 'rb'))

        if filepaths != None:
            try:
                self._intent_path = filepaths["intents"]
                self._model_path = filepaths['model-binary']
                self._words_path = filepaths['words']
                self._labels_path = filepaths['classes']
                self.intents = json.loads(open().read())
                self.model = load_model(self._model_path)
                self.words = pickle.load(open(self._words_path, 'rb'))
                self.labels = pickle.load(open(self._labels_path, 'rb'))
            except Exception as e:
                # _load_default()
                # throw exception here
                print(e)
        else:
            _load_default()
            pass

    def save(self, filepaths: dict):
        # TODO implement this method
        pass

    def _lemmatize(self, message) -> list:
        """
            This is an internal function called for tokenizing all
            the sentences into a unique set of words to be learned by
            the bot.

           :param message:
           :return:
           """
        # TODO rename this method, create docuemntation, assesss parameters
        # tokenize the pattern - splitting words into array
        tokens = nltk.word_tokenize(message)
        # print(len(tokens))
        # stemming every word - reducing to base form
        tokens = [self.lemmatize(word.lower()) for word in tokens]
        return tokens

    def _create_bag_of_words(self, tokens, show_details=True):
        """
        This is the internal function utilized to perform the hot 
        encoding of the set of words to be learned by the model.

        :param message:
        :param words:
        :param show_details:
        :return:
        """
        # TODO rename this method, create docuemntation, assesss parameters
        """  return bag of words array: 0 or 1 for words that exist in message """
        # bag of words - vocabulary matrix
        bag = [0] * len(self.words)
        for s in tokens:
            for i, word in enumerate(self.words):
                if word == s:
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    if show_details:
                        # print("found in bag: %s" % word)
                        pass
        return (np.array(bag))

    def classify(self, message) -> list:
        """
        This is the function called for predicting the intent
        of a given input sentence and the confidence of the model
        backing the prediction of the intent.

        :param message:
        :return:
        """
        # filter below  threshold predictions
        p = self._create_bag_of_words(message, self.words)
        res = self.model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        # sorting strength probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        # TODO does this ever return a list size greater than 1?
        for r in results:
            return_list.append({"intent": self.labels[r[0]],
                                "probability": str(r[1])})
        return return_list

    def generate_response(self, message: str) -> str:
        """
        This is the function to be called for generating an
        output response message from an input message. The 
        bot classifies the input message, then proceeds to 
        formulate an output based upon its trained responses.
        """
        label = self.classify(message)
        tag = label[0]['intent']
        list_of_intents = self.intents['intents']
        for i in list_of_intents:
            # this will potentially break for the oos model
            if (i['tag'] == tag):
                # output message is selected here
                result = random.choice(i['responses']) # current implementation is a randomized selection from the set of responsese
                break
        self.input_message = message
        self.label_probability = label
        self.output_message = result
        return result


if __name__ == "__main__":
    bot = ChatBot()
    bot.load()
    message = "Hi! How are you doing?"
    output = bot.generate_response(message)
    print("Bot:", output)
