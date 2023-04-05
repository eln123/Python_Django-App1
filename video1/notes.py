# Django tutorial - Setup, Installation, and Page Navigation

# look at cred.py for important info on key



# video 1 is about setting up project (installation), how Django works, getting the server running, 
# Other videos are about databases, templates, etc. 


# Django is a fullstack web framework that allows you to create websites with pure Python and a little bit of html
# This is great because typically when you make websites, you need a combination of Javascript, HTML, CSS, PHP, etc.
    # if you know Python, Django is a good way to create nice and fully functional websites



# Installation
    # command: pip3 install django
    # if you hit enter and doesn't work, he has a video for what to do

# Getting started
    # he is working in a virtual environment, so he does the command "activate django"

    # to create a project, do the command: django-admin startproject name_of_project 
            # - you can't name the project anything that is a python package, like numpi or pygame
            # - what I did, is cd to mysite and did: django-admin startproject mysite
                    # - this will create a folder called mysite, with files in it, and a manage.py file next to the folder

    # you can test if the project is working by running a server on local machine, that connects you to the website
            # the website is not live on the internet, but when you run it, it will be as if it's live on the internet, but it isn't, it's just on your local machine
            # to run it, you run the manage.py file, with a few arguments
            # command: python3 manage.py runserver 

    # if you don't want to run on port 8000, which is the one they put you on (you can see in the terminal), just type the number you want it on at the end of the command

    # now we are going to create an app 
        # to do this, we need to use the manage.py file
        # command: python3 manage.py startapp name_of_app_you_want_to_create
            # this should create a new directory in the mysite directory, called main


    # modify the .py files they give you to add html
            # be very careful, any slight mistakes can mess it up

            #1) Go to main folder
            #2) Go to views.py
                    # these are the views for your application
                    # a view is basically a web page
                        # where you write the code that serves the http requests
            #3) Once you get to views.py:
                    # from django.http import HttpResponse
                    # then, you create a function that represents a view
                    # ex: def index(response):
                        # return HttpResponse("tech with tim")
                    #   the HttpResponse function takes in HTML code
                    # you can also do: return HttpResponse("<h1>tech with tim</h1>")

            # 4) Create a file inside the main folder called, urls.py
                    # in there, we are going to write the paths to our different web pages (views)
                    # in urls.py:
                        # from django.urls import path
                        # from . import views

                        # urlpatterns = [
                        #     path("", views.index, name="index")
                        # ]

            # 5) Now we have to link the application (main folder) to our project (the video1 folder)
                    # he said this should sound confusing
                    # we need to link them, by setting a url to the app, because we can have more than one application inside our project
                    # to do this, go to the urls.py inside of the 2nd mysite folder (the one on the same level as the main folder)
                    # there should be code written in there already
                    # where it says from django.urls import path
                        # add ", include"
                        # next to import path
                    # there will already be a path in urlpatterns called "/admin"
                    # add '', include("main.urls")
                        # this means if you don't type anything in your path, it will direct us to the main.urls file
                        # basally, this is like app.use with express, it is routing you


            



                    


#________________________________________________________________
# ProgrammingHub notes:
        # Languages like PHP, Java, Python, and more help in developing Backend.
            # Django helps building the backend using Python.
            # Django is a high-level Python web framework.
            # It helps to maintain rapid development and clean, pragmatic design.
            # Django makes it easier to build better web apps quickly and with less coding effort

# Django comes with the following design philosophies:
        # Loosely Coupled − Django aims to make each element of its stack independent of the others.
        # Less Coding − Less code means a quick development.
        # Don't Repeat Yourself (DRY) − Everything should be developed only in exactly one place.
        # Clean Design − Django strictly maintains a clean design throughout its code and makes it easy to follow the best web-development practices

# Advantages of Django
# Here are few advantages of using Django which can be listed out here:
    # Object-Relational Mapping (ORM) Support − Django provides a bridge between the data model and the database engine and supports a large set of database systems, including MySQL, Oracle, Postgres, etc.
    # Multilingual Support − Django supports multilingual websites through its built-in internationalization system. So you can develop your website, which would support multiple languages.
    # Framework Support − Django has built-in support for Ajax, RSS, Caching, and various other frameworks.
    # Administration GUI − Django provides a nice ready-to-use user interface for administrative activities.
    # Development Environment − Django comes with a lightweight webserver to facilitate end-to-end application development and testing

# Django development environment consists of:
    # Installing and setting up Python
    # Installing and setting up Django
    # And a Database System.