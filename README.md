# pychatbot

## *Installation*:

1. Clone the repository

``` sh
git clone https://github.com/henrylao/pychatbot.git
```

2. Create the virtual environment in project root directory<br>
   Windows:

```sh
python -m venv c:\path\to\myenv
```

MacOS/Linux:

```sh
python -m venv path/to/project/myenv
```

3. Activate the virtual environment<br>
   Windows:

```sh
path\to\project\myenv\Scripts\activate.bat
```

MacOS/Linux

```sh
source path/to/project/myvenv/activate
```

4. Install package dependencies

``` sh
pip install -r requirements.txt
```

## *Milestones*

* [x] Complete creation of REST API endpoint for NLP model
* [ ] Migration of model application to be deployed using Docker
* [ ] Completed documentation of the model and relevant functions used:
    * [x] Sequential Model
    * [ ] Perceptron
    * [ ] Tensor
    * [ ] Layer
    * [ ] Rectified Linear Activation Function (ReLU)
    * [ ] Soft Max Function
    * [ ] Stochastic Gradient Descent (SGD) Optimization Algorithm

* [x] Completed refactoring of codebase for OOP
* [ ] Complete testing for operating systems:
    * [x] Windows 10
    * [ ] Linux
    * [ ] MacOS     
* [ ] Complete investigation of various datasets:
    * [ ] Question-Answer
        * [ ] Question-Answer Dataset: http://www.cs.cmu.edu/~ark/QA-data/
        * [ ] Microsoft WikiQA
          Corpus: https://www.microsoft.com/en-us/download/details.aspx?id=52419&from=http%3A%2F%2Fresearch.microsoft.com%2Fapps%2Fmobile%2Fdownload.aspx%3Fp%3D4495da01-db8c-4041-a7f6-7984a4f6a905
    * [ ] Customer Support
    *   [ ] Twitter: https://www.kaggle.com/thoughtvector/customer-support-on-twitter
        * [ ] Commerical IVA (train, airline, telecom): https://nextit-public.s3-us-west-2.amazonaws.com/rsics.html
        * [ ] Ubuntu: https://www.kaggle.com/rtatman/ubuntu-dialogue-corpus
    * [ ] Dialogue
        * [ ] Movie Dialogs: http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html
        * [ ] ConvAI3: Open-Domain Dialogue Systems: http://convai.io/data/
        * [ ] Spoken American English: https://www.linguistics.ucsb.edu/research/santa-barbara-corpus
        * [ ] NPS Chat Corpus: http://faculty.nps.edu/cmartell/NPSChat.htm

## *References*
#### Modular Application Development
* Application Factory Pattern: https://flask.palletsprojects.com/en/0.12.x/patterns/appfactories/
* Flask and Creating Modular Apps: https://flask.palletsprojects.com/en/0.12.x/blueprints/#blueprints
#### Server Deployment using Docker

#### Website + REST API Server:

* https://florimond.dev/blog/articles/2019/03/real-time-chatbot-server-python-bocadillo/
* Reference ChatterBot for migration of model to a class
    - https://github.com/gunthercox/ChatterBot
* Website Development:
    - https://www.youtube.com/watch?v=dam0GPOAvVI&t=1901s&ab_channel=TechWithTim
* REST API Development:
    - https://www.youtube.com/watch?v=GMppyAPbLYk&ab_channel=TechWithTim
    - https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166
    - production project file
      structure: https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/


#### Datasets:

* https://github.com/clinc/oos-eval
* https://www.kaggle.com/elvinagammed/chatbots-intent-recognition-dataset

#### Project Base:

* https://www.techwithtim.net/tutorials/ai-chatbot/part-1/
* https://dzone.com/articles/python-chatbot-project-build-your-first-python-pro
* https://www.youtube.com/watch?v=GMppyAPbLYk&ab_channel=TechWithTim

#### Libraries for NLP:

* Natural Language ToolKit
* Gensim
* Polyglot
* Dialogflow
* Tensorflow

### Libraries for Python Web Dev:

* Bocadillo
* Flask
* Django
