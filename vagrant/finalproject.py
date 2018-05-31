from flask import Flask, render_template, url_for, redirect,request
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_final import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu_final.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
@app.route("/restaurants")
def showRestaurants():
	restaurants = session.query(Restaurant).all()

	return render_template('restaurants.html')


@app.route("/restaurant/new/", methods=['GET','POST'])
def newRestaurant():

	if request.method == "POST":
		newRestaurant = Restaurant(name = request.form['name'], description = request.form['description'])
		session.add(newRestaurant)
		session.commit()
		return redirect(url_for('showRestaurants'))
	else:
<<<<<<< HEAD
		return render_template('newrestaurant.html')
||||||| merged common ancestors
		return render_template('newrestaurant.html', restaurant=restaurant, restaurant_id=restaurant_id)
=======
		return render_template('newrestaurant.html')

>>>>>>> master

@app.route("/restaurant/<int:restaurant_id>/edit", methods=['GET','POST'])

def editRestaurant(restaurant_id):
	editedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()

	if request.method == "POST":
		if request.form['name']:
			editedRestaurant.name = request.form['name']

		if request.form['description']:
			editedRestaurant.description = request.form['description']

		if request.form['price']:
			editedRestaurant.price = request.form['price']

		session.add(editedRestaurant)
		session.commit()
		return redirect(url_for(showRestaurants))

	else:
		return render_template('editrestaurant.html',restaurant_id = restaurant_id)




<<<<<<< HEAD
||||||| merged common ancestors
	return render_template('editrestaurant.html', restaurant_id=restaurant_id, restaurant=restaurant)
=======
	return render_template('editrestaurant.html', restaurant=restaurant)
>>>>>>> master


@app.route("/restaurant/<int:restaurant_id>/delete")
def deleteRestaurant(restaurant_id):
	return render_template('deleterestaurant.html')


@app.route("/restaurant/restaurant_id/menu")
def showMenu():
	return render_template('menu.html', items=items)

@app.route("/restaurant/restaurant_id/menu_id/new")
def newMenuItem():
	return render_template('newmenuitem.html')


@app.route("/restaurant/restaurant_id/menu/menu_id/edit")
def editMenuItem():
	return render_template('editmenuitem.html')

@app.route("/restaurant/restaurant_id/menu/menu_id/delete")
def deleteMenuItem():
	return render_template('deletemenuitem.html')


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)