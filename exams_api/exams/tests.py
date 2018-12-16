# Create your tests here.

from rest_framework.reverse import reverse
from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory

try:
        from models import Exam
except ImportError:
        #for tests, that are called from manage.py one directory level down
        from exams.models import Exam


from users.models import User
from examtasks.models import Examtask


class TestsOfCreating(TestCase):

    def testofcreatinguser(self):
        user_example_1 = User.objects.create(
            username='bardzik', 
            password='mypass1',
        )
        user_example_2 = User.objects.create(
            username='user_example_no2_xd',
            password='other_side_of_me',
        )


    def testforcreatingexams(self):
        user_example_1 = User.objects.create(
            username='bardzik', 
            password='mypass1',
        )
        exam_example_1 = Exam.objects.create(
            examname='exam_example_no1',
            user=user_example_1,
        )
        exam_example_2 = Exam.objects.create(
            examname='exam_example_no2_xd',
            user=user_example_1,
        )

        examtask_example_1=Examtask.objects.create(
            exam=exam_example_1,
            taskname="task no 1 ",
            user=user_example_1,
            taskdescription="sum: 2+2 is equal to...?",
            points=10,
            rightanswer="4",
        )
        factory = APIRequestFactory()
        response1 = factory.post(reverse('exams:exams-list'),exam_example_1, content_type='application/json')
        self.assertEqual(response1, exam_example_1.pk)
