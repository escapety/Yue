from django.test import TestCase
from . import models

# tests left

class BackEndTest(TestCase):
    def setUp(self):
        for i in range(4):
            models.User.objects.create(name = 'testuser' + str(i), password = '123456')
        models.Activity.objects.create(name='testact',theme='testtheme',location='peking',
                               time='2020-05-01 13:00', deadline='2020-05-01 14:00',
                               sponsor=1, introduction='testintr',complaint_num=0,
                                       type=0, attr='test')


    def test_authentication(self):
        res = self.client.get("/BackEnd/authentication",
                              {"name":"testuser0", "password": "123456"}, follow=True)

    def test_new_activity(self):
        res = self.client.get("/BackEnd/new_activity",
                              {'name':'testact','theme':'testtheme','location':'peking',
                               'time':'2020-05-01 13:00', 'deadline':'2020-05-01 14:00',
                               'sponsor':1, 'intr':'testintr','type':0, 'attr':'test'},follow=True)
        self.assertEqual(res.json()['act_id'], 2)

    def test_get_signed_up_activities(self):
        self.client.get('/BackEnd/sign_up_activity/', {'userid': '1', 'actid': '1'}, follow=True)
        res = self.client.get('/BackEnd/get_signed_up_activities/', {'userid':'1'})
        self.assertIn(1, list(res.json()['data']))

    def test_join_activity(self):
        res = self.client.get('/BackEnd/join_activity/', {'userid': '3', 'actid': '2'}, follow=True)
        join = models.Join.objects.get(user=3)
        self.assertEqual(join.activity, 2)

    def test_get_joined_activities(self):
        # 没做actid的参数校验?
        self.client.get('/BackEnd/join_activity/', {'userid': '3', 'actid': '100000'}, follow=True)
        res = self.client.get('/BackEnd/get_joined_activities/', {'userid':'3'}, follow=True)
        self.assertIn(100000, list(res.json()['data']))

    def test_get_all_activities(self):
        res = self.client.get("/BackEnd/get_all_activities", follow=True)
        self.assertEqual(1, len(list(res.json()['data'])))

    def test_get_activity(self):
        res = self.client.get("/BackEnd/get_activity/", {'id':'1'}, follow=True)
        act = models.Activity.objects.get(id=1)
        self.assertEqual(res.json()['location'], act.location)

    def test_comment(self):
        self.client.get("/BackEnd/comment/",
                              {'userid':'1', 'actid':'1', 'comment':'very bad'}, follow=True)
        comment = models.Comment.objects.get(user_id=1, act_id=1)
        self.assertEqual("very bad", comment.text)

    def test_get_user_comments(self):
        self.client.get("/BackEnd/comment/",
                              {'userid':'1', 'actid':'1', 'comment':'very bad'}, follow=True)
        res = self.client.get('/BackEnd/get_user_comments/', {'userid':1}, follow=True)
        self.assertEqual(1, len(list(res.json())))








