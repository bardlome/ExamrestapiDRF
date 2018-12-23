# Create your tests here.

from rest_framework.reverse import reverse
from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory

from exams.models import Exam


from users.models import User
from examtasks.models import Examtask


class TestsOfCreating(TestCase):

    def testofcreatinguser(self):
        self.user_example_1 = User.objects.create(
            username='bardzik', 
            password='mypass1',
        )
        self.user_example_2 = User.objects.create(
            username='user_example_no2_xd',
            password='other_side_of_me',
        )
        self.user_example_1.save()
        c = Client()
        self.response = c.post('/users/', {'username':'user_example_1.username','password':'user_example_1.password'})
        self.assertEqual(self.response.status_code, 201)

    def testforcreatingexams(self):

        self.user_example_1 = User.objects.create(
            username='bardzik', 
            password='mypass1',
        )
        self.user_example_1.save()
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='bardzik', password='mypass1')[0])




        self.exam_example_1 = Exam.objects.create(
            name='exam_example_no1',
            user=self.user_example_1
        )
        self.exam_example_1 = Exam.objects.create(
            name='exam_example_no2_xd',
            user=self.user_example_1,
        )
        self.exam_example_1.save()

        self.response = self.client.post('/exams/', {
        'user': 'self.user_example_1',
        'name': 'self.exam_example_1.name',
        'created': 'self.exam_example_1.created',
        'exam_id': 'self.exam_example_1.exam_id',
        'examtasks': 'self.exam_example_1.examtasks',
        
        })
        self.assertEqual(self.response.status_code, 201)


    def testforcreatingexamtasks(self):


        self.user_example_1 = User.objects.create(
            username='bardzik', 
            password='mypass1',
        )
        self.user_example_1.save()
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='bardzik', password='mypass1')[0])
        self.exam_example_1 = Exam.objects.create(
            name='exam_example_no1',
            user=self.user_example_1,
        )

        self.examtask_example_1=Examtask.objects.create(
            exam=self.exam_example_1,
            taskname="task no 1 ",
            taskdescription="sum: 2+2 is equal to...?",
            points=10,
            rightanswer="4",
        )
        self.examtask_example_2=Examtask.objects.create(
            exam=self.exam_example_1,
            taskname="task no 2 ",
            taskdescription="what is the color of a red 'maluch' (aka fiat 126p)?",
            points=3,
            rightanswer="red",
        )

        self.uerelka='/examtasks/{pk}/createnew/'.format(pk=self.exam_example_1.id)
        #print (self.uerelka)
        self.response = self.client.post(self.uerelka, {
        'exam':'self.examtask_example_1.exam',
        'taskname':'self.examtask_example_1.taskname',
        'rightanswer':'self.examtask_example_1.rightanswer',
        'points': self.examtask_example_1.points,
        'created':'self.examtask_example_1.created',
        'examtask_id':'self.examtask_example_1.examtask_id',
        'taskdescription':'self.examtask_example_1.taskdescription'
        })
        #print (self.response.data)
        self.assertEqual(self.response.status_code, 201)

        
