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

## *References*
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
  - production project file structure: https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/

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
