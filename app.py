from flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from meth.libr import match,additional
import collections
import random
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
ma = Marshmallow(app)
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    food = db.Column(db.String,unique=True)

class FoodSchema(ma.Schema):
    class Meta:
        fields = ('id','food')

person = FoodSchema()
persons = FoodSchema(many=True)

@app.route('/newFood', methods=["POST"])
def add_food():
    food = request.json['food']
    new_food = Food(food=food)
    existing_food = []
    all_food = Food.query.all()
    result = persons.dump(all_food)
    for i in range(len(result)):
    	existing_food.append(result[i]['food'])
    	if new_food.food in existing_food:
    		return "Food already exists"
    db.session.add(new_food)
    db.session.commit()
    return jsonify(person.dump(new_food))

@app.route('/list', methods=["GET"])
def get_food():
    all_food = Food.query.all()
    result = persons.dump(all_food)
    return jsonify(result)

@app.route('/food/update/<int:id>',methods=["PUT"])
def update_food(id):
    food_data = Food.query.get(id)
    if food_data == None:
    	return "No such id exists"
    food_data.food = request.json['food']
    db.session.commit()
    return jsonify(person.dump(food_data))

@app.route('/food/delete/<int:id>',methods=["DELETE"])
def delete_food(id):
    food_data = Food.query.get(id)
    if food_data == None:
    	return "No such id exists"
    db.session.delete(food_data)
    db.session.commit()
    return jsonify(person.dump(food_data))
    
@app.route('/menu', methods=["GET"])
def food_menu():
    all_food = Food.query.all()
    result = persons.dump(all_food)
    food_items = []
    for ele in range(len(result)):
    	food_items.append(result[ele]['food'])
    if(len(food_items)<7):
            return "Not enough food items in the list"
    days = {}
    for i in range(7):
    	days[i] = []
    for i in match(food_items):
    	days[0].append(food_items[i])
    #print(food_items)
    for i in range(1,7):
        text = []
        text=[x for x in match(food_items) if x not in days[i-1]]
        while len(text)!=3:
            x=additional(days,i,food_items)
            text.append(x.__next__())
        for j in text:
            days[i].append(food_items[j])
    weekDays = ['1 Monday','2 Tuesday','3 Wednesday','4 Thursday','5 Friday','6 Saturday','7 Sunday']
    result = {}
    for i in days.keys():
    	result[weekDays[i]] = days[i]
    return jsonify(result)   
    
if __name__ == '__main__':
    app.run(debug=True)
