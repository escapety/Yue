from django.test import TestCase
from . import models
from django.test import Client
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

#获取用户已报名的活动
class TestUnit_get_signed_up_activities(TestCase):

	def setUp(self):
		self.client = Client(enforce_csrf_checks=True)
		models.Sign_up.objects.create(user = 1, activity = 11)
		models.Sign_up.objects.create(user = 1, activity = 12)
		models.Sign_up.objects.create(user = 1, activity = 13)
		models.Sign_up.objects.create(user = 3, activity = 12)
		models.Sign_up.objects.create(user = 3, activity = 13)
		models.Sign_up.objects.create(user = 3, activity = 14)

	# 正确获得报名的活动
	def test_func_successful(self):
		response = self.client.get('/BackEnd/get_signed_up_activities/',{'userid':3})
		response = response.json()
		response = response['data']
		ideal = [12,13,14]
		self.assertEqual(ideal, response)

	# 用户没有已报名的活动
	def test_func_fail(self):
		response = self.client.get('/BackEnd/get_signed_up_activities/',{'userid':2})
		response = response.json()
		response = response['data']
		ideal = []
		self.assertEqual(ideal, response)

#创建新活动
class TestUnit_new_activity(TestCase):
	
	def setUp(self):
		self.client = Client(enforce_csrf_checks=True)

	# 正确创建新活动
	def test_func_successful(self):
		response = self.client.get('/BackEnd/new_activity/',
			{'name':'c车fsadv2323454gdfbdbfdgdsggsfdgdgfRgfds$#',
			'theme':'c车fsadv2323fdsg454@!R$#',
			'location':'c车fsa323454@!R$#',
			'time':'2020-05-20 12:12',
			'deadline':'2020-05-30 12:12',
			'sponsor': 4,
			'intr':'c车fsadv2323454@!R$#成为到处都是',
			'type':4,
			'attr':'c车fsadv2323!R$#'})
		#print(response.content)
		self.assertEqual(response.content, b'OK')


	# 新活动格式不合法
	def test_func_fail(self):
		response = self.client.get('/BackEnd/new_activity/',
			{'name':'c车fsadv2323454@!rsdfdgdfgsdgfsrggdfbgfxnxfghxfgfnxfncbvngxghfghgvbxdfgbdbfdgdsggsfdgdgfRgfds$#',
			'theme':'c车fsadv2323fdsg454@!R$#',
			'location':'c车fsa323454@!R$#',
			'time':'2020-05-20 12:12',
			'deadline':'2020-05-30 12:12',
			'sponsor': 4,
			'intr':'c车fsadv2323454@!R$#成为到处都是',
			'type':4,
			'attr':'c车fsadv2323!R$#'})
		#print(response.content)
		self.assertEqual(response.content, b'OK')

#获取活动具体信息
class TestUnit_get_activity(TestCase):

	def setUp(self):
		self.client = Client(enforce_csrf_checks=True)

		models.Activity.objects.create(name='gsfggfsdgdg',theme='gdagdherthfbxf陈法为辅￥@#@%￥4534',
			location='gsdfgg',time='2020-05-20 12:12',deadline='2020-05-25 12:12',sponsor=0,
			introduction='fsfsgdfgr',complaint_num=0,type=4,attr='fdgsg')
		models.Activity.objects.create(name='gsmghg',theme='gdagd4',
			location='gsdfgg',time='2020-05-20 12:12',deadline='2020-05-25 12:12',sponsor=1,
			introduction='fsfr',complaint_num=0,type=4,attr='fdgsg')
		
		models.Sign_up.objects.create(user = 2, activity = 2)
		models.Sign_up.objects.create(user = 1, activity = 2)
		models.Sign_up.objects.create(user = 4, activity = 2)
		models.Sign_up.objects.create(user = 7, activity = 1)
		
		models.Join.objects.create(user = 2, activity = 2)
		models.Join.objects.create(user = 3, activity = 2)
		models.Join.objects.create(user = 5, activity = 1)
		models.Join.objects.create(user = 6, activity = 1)
		models.Join.objects.create(user = 0, activity = 1)

	# 正确获得活动信息
	def test_func_successful(self):
		print('1')
		response = self.client.get('/BackEnd/get_activity/', {'id':1})
		response = response.json()
		print(response)
		#self.assertEqual(response, 'OK')


	# 没有正确获得活动信息
	def test_func_fail(self):
		print('2')
		response = self.client.get('/BackEnd/get_activity/', {'id':2})
		response = response.json()
		print(response)
		#self.assertEqual(response, 'OK')

 #将已报名用户拉入活动
class TestUnit_join_activity(TestCase):

	def setUp(self):
		self.client = Client(enforce_csrf_checks=True)
		models.Join.objects.create(user = 1, activity = 1)
	
	# 将用户拉入活动
	def test_func_successful(self):
		response = self.client.get('/BackEnd/join_activity/', {'userid':0,'actid':0})
		#print(response.content)
		self.assertEqual(response.content, b'OK')
	

	# 同一用户不能多次参与同一活动
	def test_func_fail(self):
		response = self.client.get('/BackEnd/join_activity/', {'userid':1,'actid':1})
		#print(response.content)
		self.assertEqual(response.content, b'Error')

