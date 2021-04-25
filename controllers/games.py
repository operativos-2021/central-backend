from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from webscraping.process import doProcess

#example to commit variables
# person_post_args = reqparse.RequestParser()
# person_post_args.add_argument("age",type=int,help="peson age", required=True)
# person_post_args.add_argument("gender",type=str,help="person gender", required=True)

# persons = {"juana":{"age":19,"gender":"mujer"},"juan":{"age":20,"gender":"hombre"}}

class games(Resource):
    # def get(self,name):
    #     if name not in persons:
    #         abort(400,message="Person not exist")
    #     return {"data":persons[name]}
    # def post(self,name):

    #     args = person_post_args.parse_args()
    #     persons[name] = args
    #     return persons[name],201
    def get(self):
        return {"data":doProcess()}