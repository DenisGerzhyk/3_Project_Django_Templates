# 3_Project_Django_Templates

This is a Django project that defines a model called Users with two fields: name and email. The project includes a form to create new users and a view to display all the users in the database.

The Users model is defined in the models.py file and extends the models.Model class. It has two fields: name, which is a CharField with a maximum length of 100 characters, and email, which is an EmailField with a maximum length of 100 characters. The __str__ method is defined to return a string representation of the user's name and email.

The index function is defined in views.py to handle requests to the homepage of the project. If the request is a POST request, the function creates a new UsersForm object using the POST data and saves it to the database if it is valid. Then, it redirects the user to the display view. If the request is a GET request, it creates a new, empty UsersForm object and passes it to the index.html template as part of the context.

The display function is also defined in views.py to handle requests to the display page, which shows a list of all the users in the database. It retrieves all the users from the database using Users.objects.all() and passes them to the display.html template as part of the context.

The UsersForm class in forms.py extends the ModelForm class and defines a form for the Users model. It includes fields for the name and email attributes of the Users model.
