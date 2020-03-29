from flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
ma = Marshmallow(app)
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    food = db.Column(db.String)

class FoodSchema(ma.Schema):
    class Meta:
        fields = ('id','food')

person = FoodSchema()
persons = FoodSchema(many=True)



@app.route('/newFood', methods=["POST"])
def add_food():
    food = request.json['food']
    new_food = Food(food=food)
    db.session.add(new_food)
    db.session.commit()
    return jsonify(person.dump(new_food))

@app.route('/menu', methods=["GET"])
def get_food():
    all_food = Food.query.all()
    result = persons.dump(all_food)
    return jsonify(result)

@app.route('/food/update/<int:id>',methods=["PUT"])
def get_peron(id):
    food_data = Food.query.get(id)
    food_data.food = request.json['food']
    db.session.commit()
    return jsonify(person.dump(food_data))

@app.route('/food/delete/<int:id>',methods=["DELETE"])
def delete_food(id):
    food_data = Food.query.get(id)
    db.session.delete(food_data)
    db.session.commit()
    return jsonify(person.dump(food_data))



if __name__ == '__main__':
    app.run(debug=True)
