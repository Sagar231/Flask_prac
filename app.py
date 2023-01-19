from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

stores = [
    {    'name' : 'my wonderful store',
         'items':[
             {
                 'name': 'my item',
                 'price': 15.99
             }
         ]
     }
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/store",methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store={
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route("/store/<string:name>")
def get_store(name):
    for _ in stores:
        if _['name']==name:
            return jsonify(_)
    return jsonify({"massage":"The store was not found"})

@app.route("/store")
def get_stores():
    return jsonify({"stores":stores})

@app.route("/store/<string:name>/item",methods = ["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for _ in stores:
        if _['name']==name:
            new_item ={
                "name" : request_data["name"],
                "price": request_data["price"]
            }
            _['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({"massage":"store not found"})

@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for _ in stores:
        if _['name']==name:
            return jsonify({"items": _['items']})
    return jsonify({"massage":"The item was not found"})

app.run(port = 5000)