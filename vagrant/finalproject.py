from flask import Flask, render_template, url_for, redirect,request, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_final import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu_final.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Making an API endpoint(GET request)
@app.route('/restaurants/JSON')
def restaurantsJSON():
	restaurants = session.query(Restaurant).all()
	return jsonify(restaurantjson = [test.serialize for test in restaurants])



@app.route("/")
@app.route("/restaurants")
def showRestaurants():
	restaurants = session.query(Restaurant).all()

	for n in restaurants:
		restaurant_id = n.id
		restaurant_name = n.name
		#print restaurant_name

	return render_template('restaurants.html',restaurants=restaurants, restaurant_id=restaurant_id, restaurant_name=restaurant_name)


@app.route("/restaurant/new/", methods=['GET','POST'])
def newRestaurant():

	if request.method == "POST":
		newRestaurant = Restaurant(name = request.form['name'], description = request.form['description'])
		session.add(newRestaurant)
		session.commit()
		return redirect(url_for('showRestaurants'))
	else:
		return render_template('newrestaurant.html')

@app.route("/restaurant/<int:restaurant_id>/edit", methods=['GET','POST'])

def editRestaurant(restaurant_id):
	editedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).first()

	if request.method == "POST":
		if request.form.get('name', False):
			editedRestaurant.name = request.form.get('name', False)

		if request.form.get('description',False):
			editedRestaurant.description = request.form.get('description',False)

		if request.form.get('price', False):
			editedRestaurant.price = request.form.get('price', False)

		session.add(editedRestaurant)
		session.commit()
		return redirect(url_for('showRestaurants'))

	else:
		return render_template('editrestaurant.html',restaurant_id = restaurant_id, restaurant_name=editedRestaurant.name)


@app.route("/restaurant/<int:restaurant_id>/delete", methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
	deletedRestaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	
	if request.method == "POST":
		session.delete(deletedRestaurant)
		session.commit()
		return redirect(url_for('showRestaurants'))

		pass
	return render_template('deleterestaurant.html', restaurant_id=restaurant_id, restaurant_name=deletedRestaurant.name)


@app.route("/restaurant/<int:restaurant_id>/menu")
def showMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)

	return render_template('menu.html', restaurant_id=restaurant_id, restaurant_name=restaurant.name, items=items)


@app.route("/restaurant/<int:restaurant_id>/new", methods=["GET","POST"])
def newMenuItem(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)

	for m in items:
		menu_id = m.id
		menu_name = m.name
		print menu_id

	if request.method == 'POST':
		newItem = MenuItem(name = request.form['name'], description = request.form['description'], price = request.form['price'],restaurant_id = restaurant_id)
		session.add(newItem)
		session.commit()
		return redirect(url_for('showMenu', restaurant_id = restaurant_id))

	return render_template('newmenuitem.html', restaurant_id=restaurant_id, restaurant_name=restaurant.name)


@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit", methods=["GET","POST"])
def editMenuItem(restaurant_id, menu_id):
	editedItems = session.query(MenuItem).filter_by(id = menu_id).one()
	menu_name = editedItems.name

	if request.method == 'POST':
		if request.form['name']:
			editedItems.name = request.form['name']
		if request.form['description']:
			editedItems.description = request.form['name']
		if request.form['price']:
			editedItems.price = request.form['price']

		session.add(editedItems)
		session.commit()
		return redirect(url_for('showMenu', restaurant_id = restaurant_id))

	return render_template('editmenuitem.html',menu_id= menu_id, restaurant_id = restaurant_id , menu_name=menu_name)

@app.route("/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete", methods=["GET","POST"])
def deleteMenuItem(restaurant_id, menu_id):
	editedItems = session.query(MenuItem).filter_by(id = menu_id).one()
	menu_name = editedItems.name

	if request.method == "POST":
		session.delete(editedItems)
		session.commit()
		return redirect(url_for('showMenu', restaurant_id = restaurant_id))


	return render_template('deletemenuitem.html', menu_id= menu_id, restaurant_id = restaurant_id , menu_name=menu_name)


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)