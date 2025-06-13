
from flask import Flask

from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi' : {'item' :'2 ltr bottle', 'price' :120, 'qty' :250},
    'coke' :{'item' :'500 ml bottle', 'price' :60, 'qty' :350},
    'thumbs_up' :{'item' :'300 ml can', 'price' :50, 'qty' :100}
}

class Products(Resource):

    def get(self, product):
        return {product :products[product]}

api.add_resource(Products, "/getproduct/<product>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader = True)