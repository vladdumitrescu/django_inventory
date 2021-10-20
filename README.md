**About**

Webpage for a drone inventory system using the Python Django framework.

### Notice before deploy

Please take note that the chosen back-end database for data storage is MySQL, the development platform was Windows and that XAMPP was used.

Therefore, make sure to install XAMPP beforehand and start the apache and msql services.

The database needs to be created as well, django_drone_db.

You can find the database configurations in django_inventory/drone_management/drone_management/settings.py

* Change directory to django_inventory/drone_management/drone_management/ 
* Run the following commands:
```django
python manage.py makemigrations 
python manage.py migrate   
```
The first command creates the migrations from the models, while the second applies the migrations in the database.

* Next we need to create a superuser for the login step, default values should suffice:
```django
python manage.py createsuperuser
```


### Start the server:

* Change directory to django_inventory/drone_management/drone_management/
* Run the following command:
```django
python manage.py runserver
```

### Django admin

Login with your generated credentials.

You can explore the Django admin and start adding values in Drones and Camera brands.

Filter functionality was provided by Django.

!Note: values in Camera Brands are needed for the localhost filter functionality.

### Localhost

Check the  http://127.0.0.1:8000/ URL.

You should not see any values here on the first run.

In order to add them, you need login or register first (credentials from createsuperuser are valid here as well).

The Add Drone functionality should be avaiable now.

You can also update or delete(not available if not logged in) values when clicking on the "Detail" button of the generated values.

Unlike the admin page, the filter functionality is more basic.

Also, the search bar checks for drone' names only.