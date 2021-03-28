from flask import Flask , request , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init app

app=Flask(__name__)

# Configuring Database Uri

base_dir=os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(base_dir , 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

# db init 
db=SQLAlchemy(app) 


# mashmallow init / for serialization 

ma=Marshmallow(app)



#Creating models 

class Product(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name=db.Column(db.String(100))
    description=db.Column(db.String(200))
    price=db.Column(db.Float)
    qty=db.Column(db.Integer)


    def __init__(self, name, description , price , qty):
        self.name=name
        self.description=description
        self.price=price
        self.qty=qty



class Product_Schema(ma.Schema):
    class Meta:
        fields=('id','name', 'description','price','qty')

single_product_schema=Product_Schema()
multi_product_schema=Product_Schema(many=True )


#Routing


# post data into database

@app.route('/add_product', methods=['POST'])

def add_post():
    name=request.json['name']
    description=request.json['description']
    price=request.json['price']
    qty=request.json['qty']

    new_product=Product(name,description,price,qty)
    db.session.add(new_product)
    db.session.commit()
    
    return single_product_schema.jsonify(new_product)


# getting all items

@app.route('/get-all/' , methods=['GET'])

def get_all_items():

    items=Product.query.all()

    return multi_product_schema.jsonify(items)






# getting details of some data throgh id

@app.route('/get-details/<id>' , methods=['GET'])

def get_data(id):

    item=Product.query.get(id)

    return single_product_schema.jsonify(item)



# deleting post

@app.route('/delete-item/<id>' , methods=['DELETE'])

def delete_item(id):
    item=Product.query.get(id)
    db.session.delete(item)
    db.session.commit()
    
    return 'product deleted'



#updating item

@app.route('/update-item/<id>' , methods=['PUT'])

def update_item(id):
    item=Product.query.get(id)
    
    item.name=request.json['name']
    item.description=request.json['description']
    item.price=request.json['price']
    item.qty=request.json['qty']


    updated_item=Product(item.name,item.description,item.price,item.qty)
    
    db.session.flush()
    db.session.commit()

    return single_product_schema.jsonify(item)




# Running the server
if __name__== '__main__':
    app.run(debug=True)
