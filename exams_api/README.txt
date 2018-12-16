Because the project is not marked as "done", I've left the api_root view, to have a better view over the project.


URLS availible:
http://127.0.0.1:8000/
 general overview

http://127.0.0.1:8000/admin/
 admin view for better managing during development

http://127.0.0.1:8000/docs/
 for a better overview during development

http://127.0.0.1:8000/users/
 request get = showing the list of users, post = registration of a new user

http://127.0.0.1:8000/users/(integer)
 request get = showing the details of the user, put = changing personal data of the user, delete = delete the user

http://127.0.0.1:8000/exams/
 request get = showing the list of exams of a specific user (required to be logged in), post = creation of a new exam for specified user

http://127.0.0.1:8000/exams/(integer)/
 request get = showing the details of the exam with id equal to provided integer, put = changing the details of the exam, delete = delete the exam

http://127.0.0.1:8000/exams/(integer)/examtasks
 request get = showing the list of examtasks of a specific exam, post = creation of a new examtask for specified exam

http://127.0.0.1:8000/exams/(integer)/examtasks/(integer2)/
 request get = showing the details of the examtask with id equal to provided integer, put = changing the details of the examtask, delete = delete the examtask


User can create a examtask of various specification. Examtasks have a field to write a title for them, their description, right answer, and points for providing the right answer.

worked under virtualenv, on Ubuntu 16.04 (example):
bardlome@bardlome-Lenovo-Z580:~/nowy2$ virtualenv --python=python3 envforchallange
bardlome@bardlome-Lenovo-Z580:~/nowy2$ source envforchallange/bin/activate 

tests.py are included in exams_api/exams, executed with command from terminal (example):
(envforchallange) bardlome@bardlome-Lenovo-Z580:~/nowy2/envforchallange/exams_api$ python3  manage.py  test  exams

to start, execute command from terminal (example):
(envforchallange) bardlome@bardlome-Lenovo-Z580:~/nowy2/envforchallange/exams_api$ python3  manage.py  runserver




