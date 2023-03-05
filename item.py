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
        item  = self.find_by_name(name)
        if item:
            return item

        return {"massage":"item not found"},404
        #most popular http code is 200

    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
    def post(self,name):
        if self.find_by_name(name):
            return {"massage":f"Item with name {name} already exixts." },400 #bad request

        data = Item.parser.parse_args()
        #get_jason(force = True//silent = true) force = True means u do not need content type header#not recommended
        item = {'name':name , 'price' : data['price']}
        try:
            self.insert(item)
        except:
            return {"massage": "An error occurred inserting the item"} , 500
        #500 = internal server error

        return item ,201
    @classmethod
    def insert(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()
    def delete(self,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()
        return {"massage":"item deleted"}

    def put(self,name):
        data = Item.parser.parse_args()

        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
               self.insert(updated_item)
            except:
                return {"massage": "An error occurred inserting the item."},500
        else:
            try:
                self.update(updated_item)
            except:
                return {"massage": "An error occurred updating the item."}, 500
        return item

    @classmethod
    def update(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'],item['name']))

        connection.commit()
        connection.close()
class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name':row[0],'price':row[1]})

        connection.close()

        return {"items":items}