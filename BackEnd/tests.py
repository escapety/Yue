from django.test import TestCase
from . import models

# Create your tests here.

class BackEndTest(TestCase):
    def setUp(self):
        models.User.objects.create(name = 'testuser', password = '123456')


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



