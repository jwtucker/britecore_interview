Installation
-----
Create a virtualenv in the directory, install django 2.*, and run the server using manage.py runserver.

Tech Stack
-----
Back-end: Django

Front-end: Vue.js

Explanation of design
-----
Django's probably overengineering the project a little but I wanted to check out Django 2.0 because I have some projects to migrate. In my opinion, Django's templating engine is pretty bad and I think it's better when Django is used as a completely decoupled back-end, but since this is a temporary project with one front-end file I just shoved it into the templating engine instead of using nginx.

I made choices in the design to fit the spirit of the project:

A noSQL solution would probably be better for this use case but since it seems like half the project is to build a properly normalized RDBMS around the data, I used SQLlite.

I didn't want a ton of dependencies and bloat, so there's no CSS, no datepicker (and since html5's datepicker is only half adopted, I just showed in markup that the value is passing correctly)

There's a lot of extra abstraction and refactoring I would do if this would grow into a real project. The vue.js component wouldn't just float around in index.html, the frontend would be decoupled in its own repo, etc.