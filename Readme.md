- To install django
`pip install dango`
- When you install Django, it actually also installed a command line tool called:
`django-admin`
- Let’s create our first project. Type:
`django-admin startproject first_project`

## Project structure
- __init__.py: This is a blank Python script that due to its special name let’s Python know that this directory can be treated as a package
- settings.py: This is where you will store all your project settings
- urls.py: This is a Python script that will store all the URL patterns for your project. Basically the different pages of your web application.
- wsgi.py: This is a Python script that acts as the Web Server Gateway Interface. It will later on help us deploy our web app to production
- manage.py: This is a Python script that we will use a lot. It will be associates with many commands as we build our web app!

## Run Server
`python manage.py runserver`

## Migration Warning
``` 
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```
### What is migration ?
- A migration allows you to move databases from one design to another, this is also reversible.

## Terminologies
- A Django Project is a collection of applications and configurations that when combined together will make up the full web application (your complete website running with Django)
- A Django Application is created to perform a particular functionality for your entire web application. For example you could have a registration app, a polling app, comments app, etc.
- These Django Apps can then be plugged into other Django Projects, so you can reuse them! (Or use other people’s apps)
- To create a simple application with: `python manage.py startapp first_app`

## Reference
https://docs.google.com/presentation/d/1XQr2C3E_jVjDvCm_Z9yZPVOAop72OP7ZatOjnJZCl-k/edit#slide=id.g1c3e28ca26_0_14