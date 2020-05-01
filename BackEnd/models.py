from django.db import models

# Create your models here.

#评论类
class Comment(models.Model):
    #评论用户ID
    user_id = models.IntegerField()
    #评论所属活动ID
    act_id = models.IntegerField()
    #评论发布时间
    time = models.DateTimeField(auto_now_add = True)
    #评论内容
    text = models.TextField()
    #评论举报数量
    complaint_num = models.IntegerField()

#活动类
class Activity(models.Model):
    #活动名
    name = models.CharField(max_length = 50)
    #活动主题
    theme = models.CharField(max_length = 50)
    #活动地点
    location = models.CharField(max_length = 50)
    #活动时间
    time = models.DateTimeField()
    #活动报名截止时间
    deadline = models.DateTimeField()
    #活动组织者编号
    sponsor = models.IntegerField()
    #活动介绍
    introduction = models.TextField()
    #活动举报数量
    complaint_num = models.IntegerField()
    #活动类别
    type = models.IntegerField()
    #活动具体属性
    attr = models.CharField(max_length = 50)
    #该活动的评论
    comments = models.ManyToManyField(Comment)

#用户类
class User(models.Model):
    #用户名
    name = models.CharField(max_length=50)
    #用户密码
    password = models.CharField(max_length=20)
    #用户信息
    info = models.CharField(max_length=100)
    #地理位置
    position = models.CharField(max_length=50)
    #评论的列表
    comments = models.ManyToManyField(Comment)

#发起的活动列表
class Organize(models.Model):
    user = models.IntegerField()
    activity = models.IntegerField()

#参与的活动列表
class Join(models.Model):
    user = models.IntegerField()
    activity = models.IntegerField()

#报名的活动列表
class Sign_up(models.Model):
    user = models.IntegerField()
    activity = models.IntegerField()

#好友列表
class Friend(models.Model):
    user1 = models.IntegerField()
    user2 = models.IntegerField()

#评论回复
class Commemt_reply(models.Model):
    comment = models.IntegerField()
    reply = models.IntegerField()