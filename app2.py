from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security2 import authenticate, identity
from user2 import UserRegister
from item import Item,ItemList
#we no more need jasonify to create json formate flask_restful does it for us

app = Flask(__name__)
app.secret_key = "Sagar_key"
api = Api(app)

jwt = JWT(app,authenticate,identity) #/auth

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

if __name__ == "__main__":
   app.run(port = 5000,debug = True)
