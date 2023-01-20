from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT ,jwt_required
from security import authenticate, identity
#we no more need jasonify to create json formate flask_restful does it for us

app = Flask(__name__)
app.secret_key = "Sagar_key"
api = Api(app)

jwt = JWT(app,authenticate,identity) #/auth

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank'
                        )


    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x: x['name']==name,items),None)
        return {"item": item} , 200 if item else 404 #most popular http code is 200

    def post(self,name):
        if next(filter(lambda x: x['name']==name,items),None):
            return {"massage":f"Item with name {self.name} already exixts." },400 #bad request

        data = Item.parser.parse_args()
        #get_jason(force = True//silent = true) force = True means u do not need content type header#not recommended
        item = {'name':name , 'price' : data['price']}
        items.append(item)
        return item ,201

    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name']!=name,items))
        return {"massage":"item deleted"}

    def put(self,name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x:x['name']==name,items),None)
        if item is None:
            item = {'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {"items":items}

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')

app.run(port = 5000,debug = True)