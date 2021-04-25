from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import sys
from controllers.games import games

app = Flask(__name__)

api = Api(app)

api.add_resource(games,"/game")
if __name__ == "__main__":
        app.run(debug=True) #app.run(debug=False)
