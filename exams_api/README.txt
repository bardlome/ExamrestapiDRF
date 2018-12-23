Because the project is not marked as "done", I've left the api_root view, to have a better view over the project.
Used version of python: Python 3.5.2
Also, an interface is an example one, from django rest.


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
 request get = showing the details of the exam with id equal to provided integer, put = changing the details of the exam, delete = delete the exam. One can also use filters there, to change the order of displayed exams.

http://127.0.0.1:8000/exams/listoftasks/(integer)/
 request get = showing the list of examtasks of a specific exam, in a convinient, "light" mode.
 
http://127.0.0.1:8000/examtasks/
 request get = showing all examtasks created
 
http://127.0.0.1:8000/examtasks/(integer)/createnew
 request get = showing the details of all examtasks, post = new examtask to an exam with id equal to provided integer
 
http://127.0.0.1:8000/examtasks/(integer)/edit
 request get = showing the details of the examtask with id equal to provided integer, put = changing the details of the examtask, delete = delete the examtask

http://127.0.0.1:8000/answers/
 request get = showing all answers created
 
http://127.0.0.1:8000/answers/(integer)/createnew
 request get = showing the details of all answers, post = new answer to an examtask with id equal to provided integer(and deleting the previous answers of that user, if there existed)

http://127.0.0.1:8000/answers/(integer)/edit
 request get = showing the details of the answer with id equal to provided integer, put = changing the details of the answer, delete = delete the answer
 
User can create a examtask of various specification. Examtasks have a field to write a title for them, their description, right answer, and points for providing the right answer. One can also post their answers by "answers" section.

worked under virtualenv, on Ubuntu 16.04 (example):
bardlome@bardlome-Lenovo-Z580:~/nowy2$ virtualenv --python=python3 envforchallange
bardlome@bardlome-Lenovo-Z580:~/nowy2$ source envforchallange/bin/activate 

tests.py are included in exams_api/exams, executed with command from terminal (example):
(envforchallange) bardlome@bardlome-Lenovo-Z580:~/nowy2/envforchallange/exams_api$ python3  manage.py  test  exams

to create suuser, execute command from terminal (example):
(envforchallange) bardlome@bardlome-Lenovo-Z580:~/nowy2/envforchallange/exams_api$ python3  manage.py  runserver

to start, execute command from terminal (example):
(envforchallange) bardlome@bardlome-Lenovo-Z580:~/nowy2/envforchallange/exams_api$ python3  manage.py  runserver


feel free to run tests from "exams" directory, and quickly check out how does it work at: http://127.0.0.1:8000/docs/
feel free to delete the example sqlite database and start your own one!
remember, that some of the functions REQUIRE an non-anonymous user(log in!)
and some views (for example exam details) require an owner to be logged in to see it!


