from django.test import TestCase
from . import models

# Create your tests here.

class BackEndTest(TestCase):
    def setUp(self):
        models.User.objects.create(name = 'testuser', password = '123456')

    def test_new_user(self):
        self.client.get('/BackEnd/new_user/', {'name':'testuser', 'password':'123456'})
        user = User.objects.get(name = 'testuser')
        self.assertEqual(user.password, '123456')
        res = self.client.get('/BackEnd/new_user/', {'name': 'testuser', 'password': '123456'})
        self.assertEqual(res.json()['errormsg'], 'FAIL: EXIST SAME NAME USER')

    def test_authentication(self):
        res = self.client.get('/BackEnd/authentication/', {'name': 'testuser2', 'password': '123456'})
        self.assertEqual(res.json()['errormsg'], 'FAIL: USER NOT EXIST')
        User.objects.create(name = 'testuser2', password = '123456')
        res = self.client.get('/BackEnd/authentication/', {'name': 'testuser2', 'password': '123456'})
        self.assertEqual(res.json()['errormsg'], 'SUCCESS')
        res = self.client.get('/BackEnd/authentication/', {'name': 'testuser2', 'password': '123457'})
        self.assertEqual(res.json()['errormsg'], 'FAIL: WRONG PASSWORD')

    def test_get_all_activities(self):
        user = User.objects.create(name='testuser3', password='123456')
        act1 = Activity.objects.create(name = 'testact', theme = 'test', location = 'test',
                                time = '2020-06-01 20:00', deadline = '2020-06-01 20:00', sponsor = user.id, introduction = 'test',
                                type = 0, attr = 'test', complaint_num = 0)
        act2 = Activity.objects.create(name='testact', theme='test', location='test',
                                time='2020-06-01 20:00', deadline='2020-06-01 20:00', sponsor = user.id, introduction='test',
                                type=0, attr='test', complaint_num = 0)
        res = self.client.get('/BackEnd/get_all_activities/')
        actlist = []
        actlist.append(act1.id)
        actlist.append(act2.id)
        self.assertEqual(res.json()['data'], actlist)

    def test_get_my_activities_test(self):
        user = User.objects.create(name='testuser3', password='123456')
        act = Activity.objects.create(name='testact1', theme='test', location='test',
                                time='2020-06-01 20:00', deadline='2020-06-01 20:00', sponsor=user.id,
                                introduction='test',
                                type=0, attr='test', complaint_num=0)
        Organize.objects.create(user = user.id, activity = act.id)
        res = self.client.get('/BackEnd/get_my_activities/', {'userid':user.id})
        actlist = []
        actlist.append(act.id)
        self.assertEqual(res.json()['data'], actlist)

    def test_get_joined_activities_test(self):
        user = User.objects.create(name='testuser3', password='123456')
        act = Activity.objects.create(name='testact1', theme='test', location='test',
                                time='2020-06-01 20:00', deadline='2020-06-01 20:00', sponsor=user.id,
                                introduction='test',
                                type=0, attr='test', complaint_num=0)
        Join.objects.create(user = user.id, activity = act.id)
        res = self.client.get('/BackEnd/get_joined_activities/', {'userid':user.id})
        actlist = []
        actlist.append(act.id)
        self.assertEqual(res.json()['data'], actlist)

    def test_sign_up_activity(self):
        self.client.get('/BackEnd/sign_up_activity/', {'userid': '1', 'actid': '1'})
        sign_up = models.Sign_up.objects.get(user = 1)
        self.assertEqual(sign_up.activity, 1)

    def test_get_act_comments(self):
        res = self.client.get('/BackEnd/get_act_comments/', {'actid': '1'})
        self.assertEqual(res.json()['data'], [])

    def test_get_comment_by_id(self):
        res = self.client.get('/BackEnd/get_comment_by_id/', {'cmtid': '1'})
        self.assertEqual(res.json()['text'], '1')

        
    def test_search_by_name(self):
        res = self.client.get('/BackEnd/search_by_name/', {'name': 'testact'})
        self.assertEqual(res.json()['sponsor'], 1)



