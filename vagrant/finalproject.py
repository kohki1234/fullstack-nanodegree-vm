from flask import Flask, render_template
app = Flask(__name__)


restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Kohki Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Kohki Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

 

@app.route("/")
@app.route("/restaurants")
def showRestaurants():
	return render_template('restaurants.html',restaurants = restaurants)


@app.route("/restaurant/new/")
def newRestaurant():
	return render_template('newrestaurant.html', restaurant = restaurant)

@app.route("/restaurant/<int:restaurant_id>/edit")
def editRestaurant(restaurant_id):
	return render_template('editrestaurant.html')


@app.route("/restaurant/<int:restaurant_id>/delete")
def deleteRestaurant(restaurant_id):
	return render_template('deleterestaurant.html')


@app.route("/restaurant/restaurant_id/menu")
def showMenu():
	return render_template('menu.html', items=items)

@app.route("/restaurant/restaurant_id/menu_id/new")
def newMenuItem():
	return "This page is for making a new menu item for restaurant " 


@app.route("/restaurant/restaurant_id/menu/menu_id/edit")
def editMenuItem():
	return "This page is for editing menu item " 

@app.route("/restaurant/restaurant_id/menu/menu_id/delete")
def deleteMenuItem():
	return "This page is for deleteing menu item "


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)