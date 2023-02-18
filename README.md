# Todo-appliction
todo application based on django

[icons](https://www.flaticon.com/): icons were used from this site

# 👋Introduction
Welcome to our Django to-do application's README page! You've come to the right place if you're looking for a dependable and effective task management solution. Our application, which is based on the Django web framework and django restframework, is made to assist you in keeping your work organised and productive.

You can easily create, read, update, and delete tasks using our application and mark them as complete once you're done. Our app is the ideal tool to help you stay on top of your to-do list, whether you're a busy professional or a student juggling multiple assignments.

In addition to our web-based task management application, our Django todo app also includes APIs that allow you to access and manipulate your tasks programmatically. With our APIs, you can integrate your tasks with other applications, build custom workflows, and automate your task management process.

Our APIs are designed to be simple, intuitive, and RESTful, allowing you to easily perform CRUD operations on your tasks. Plus our code is open-source and accessible on GitHub, you can modify it to meet your particular requirements and add to the project. Also you can customize and extend the APIs to fit your specific use case.

# 🏃‍♂️How to run the Todo application
1. Clone the repository

``` bash
git clone https://github.com/sea-rod/Todo-application.git
```
2. Change the working directory
```bash
cd Todo-application
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
or
```bash
python -m pip insatll -r requirements.txt 
```
4. Then run the `python manage.py migrate` to make create tables in the database
```bash
python manage.py migrate
```
5. Then run the `python manage.py collectstatic` command
```bash
python manage.py collectstatic
```
6. Then run the `python manage.py runserver` command to start the development server
```bash
python manage.py runserver
```
>Note: Do not use the this server for production

7. Visit the link the site hosted on in your web browser

8. Thats all your good to go. Enjoy the app 💖!!

> Information on how to use the api will be provided soon


# 🔨Built with
- [Django](https://www.djangoproject.com/): Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
- [Flaticon](https://www.flaticon.com/): Icons used in this project are from flaticon 

-[Django REST framework](https://www.django-rest-framework.org/):Django REST framework is a powerful and flexible toolkit for building Web APIs.

# License
This project is licensed under the MIT license - see [`License`](LICENSE.txt) file for details.