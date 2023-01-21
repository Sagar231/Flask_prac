from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank'
                        )


    @jwt_required()
    def get(self,name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item':{'name':row[0],'price':row[1]}}

        return {"massage":"item not found"},404
        #most popular http code is 200

    def post(self,name):
        if next(filter(lambda x: x['name']==name,items),None):
            return {"massage":f"Item with name {name} already exixts." },400 #bad request

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