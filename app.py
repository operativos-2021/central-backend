from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import sys
from controllers.games import games
from controllers.email import email
from controllers.load_balance import load_balance

app = Flask(__name__)

api = Api(app)

api.add_resource(games,"/games/<int:quantity>")
api.add_resource(load_balance,"/load_balance/<string:games_range>")
api.add_resource(email,"/email/") #Load balancing


if __name__ == "__main__":
        app. run(debug=False,port=int("5000"),host='0.0.0.0') #app.run(debug=False)