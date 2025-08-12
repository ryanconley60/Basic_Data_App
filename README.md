# Run Deployed Web Application on Python Anywhere
 For convenience, this application is currently hosted at https://ryanconley60.pythonanywhere.com/home

# Checkout and Setup
 This application was developed using django and some supporting django libraries.
 This application has only been tested in a Windows environment with python version 3.13

 To install the required dependencies, open a terminal and navigate to the installation directory
 
    $ pip install -r requirements.txt

 Navigate one directory down to the same directory as manage.py if you aren't already for more convenience running the manage.py service

    $ cd django_server

 Then simply update then apply the migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate

 You can now run the development server:

    $ python manage.py runserver

 This assumes the default configuration, the django application will be accessible on port 8000
 For example, http://127.0.0.1:8000/

 Additional wsgi configurations and/or updating the allowed urls in settings.py might be needed to cover other deployment needs


# Basic_Data_App
 Basic Flask app for data entry

 Consists of a homepage where a user enters data and a simple data page where they can view it

 The user enters data into a form with 4 fields
 It includes fields for name, age, title, and hometown
 Name and title are required fields, while age and hometown are optional

 When the user hits the submit button, it will take them to the data entry page but will show the individual row data that they submitted.

 All invalid urls that return a 404 redirect to the homepage
