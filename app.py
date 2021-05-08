from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import sys
from controllers.games import games
from controllers.email import email

app = Flask(__name__)

api = Api(app)

api.add_resource(games,"/games/<int:quantity>")
api.add_resource(email,"/email/")

if __name__ == "__main__":
        app. run(debug=True) #app.run(debug=False)