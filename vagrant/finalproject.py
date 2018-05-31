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

	return render_template('restaurants.html',restaurants=restaurants)



@app.route("/restaurant/new/", methods=['GET','POST'])
def newRestaurant():

	if request.method == "POST":
		newRestaurant = Restaurant(name = request.form['name'], description = request.form['description'])
		session.add(newRestaurant)
		session.commit()
		return redirect(url_for('showRestaurants'))
	else:
		return render_template('newrestaurant.html')





@app.route("/restaurant/<int:restaurant_id>/edit")

def editRestaurant(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()

	return render_template('editrestaurant.html', restaurant=restaurant)







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