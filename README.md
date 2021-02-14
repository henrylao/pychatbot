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
3. Activate the virtual<br>
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
pip install requirements.txt
```



## *Milestones*
* [ ] Serve model on a dedicated REST API server using Flask by creating a REST endpoint of contact
* [ ] Migration of model application to be deployed using Docker
* [ ] Completed documentation of the model and relevant functions used:
	* [x] Sequential Model
	* [ ] Perceptron
	* [ ] Tensor
	* [ ] Layer
	* [ ] Rectified Linear Activation Function (ReLU)
	* [ ] Soft Max Function
	* [ ] Stochastic Gradient Descent (SGD) Optimization Algorithm

* [ ] Completed refactoring of codebase for OOP


## *References*
#### Server Deployment using Docker

#### REST API Server:
* https://florimond.dev/blog/articles/2019/03/real-time-chatbot-server-python-bocadillo/
* Reference ChatterBot for migration of model to a class
  - https://github.com/gunthercox/ChatterBot

#### Datasets:
* https://github.com/clinc/oos-eval
* https://www.kaggle.com/elvinagammed/chatbots-intent-recognition-dataset

#### Project:
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
