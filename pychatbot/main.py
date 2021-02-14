# import utils
from flask import Flask, request
from flask_restful import reqparse, Api

from pychatbot import utils
from pychatbot.main.model.chatbot import ChatBot

app = Flask("chatbot-api")
api = Api(app)

# setup project paths
ROOT_DIR = utils.get_project_root()
CACHE_DIR = ROOT_DIR / "cache"
INPUT_DIR = ROOT_DIR / "input"

bot = ChatBot()
bot.load()

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('message', type=str, help="User message")
parser.add_argument('timestamp', type=str, help="User message")
parser.add_argument('user', type=str, help="User message")

BOT_BASE_URI = '/api/v1/bot/'

@app.route(BOT_BASE_URI + "reply", methods=['POST'])
def reply():
    if request.method == 'POST':
        args = parser.parse_args()
        output = bot.generate_response(args['message'])
        # print(output)
        output = {
            "message":"",
            "timestamp":"",
            "version":""
        }
        return output


if __name__ == '__main__':
    app.run(debug=True)
