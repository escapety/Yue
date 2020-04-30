from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from . import models

# Create your views here.
def new_user(request):
    user_name = request.GET.get('name', '')
    user_pw = request.GET.get('password', '')
    models.User.objects.create(name = user_name, password = user_pw, info = '', position = '')
    return HttpResponse("OK")

def authentication(request):
    user_name = request.GET.get('name', '')
    user_pw = request.GET.get('password', '')
    user = models.User.objects.get(name = user_name)
    if user.password == user_pw:
        return HttpResponse("OK")
    else:
        return HttpResponse("ERROR")

def get_all_activities(request):
    act_list = []
    all_act = models.Activity.objects.all()
    for act_item in all_act:
        act_list.append(act_item.id)
    ret = {
        'data':act_list,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

def get_my_activities(request):
    user_id = int(request.GET.get('userid', ''))
    act_list = []
    all_org = models.Organize.objects.all()
    for org_item in all_org:
        if org_item.user == user_id:
            act_list.append(org_item.activity)
    ret = {
        'data':act_list,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

def get_joined_activities(request):
    user_id = int(request.GET.get('userid', ''))
    act_list = []
    all_join = models.Join.objects.all()
    for join_item in all_join:
        if join_item.user == user_id:
            act_list.append(join_item.activity)
    ret = {
        'data':act_list,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

def get_signed_up_activities(request):
    user_id = int(request.GET.get('userid', ''))
    act_list = []
    all_sign_up = models.Sign_up.objects.all()
    for sign_up_item in all_sign_up:
        if sign_up_item.user == user_id:
            act_list.append(sign_up_item.activity)
    ret = {
        'data':act_list,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

def new_activity(request):
    act_name = request.GET.get('name', '')
    act_theme = request.GET.get('theme', '')
    act_location = request.GET.get('location', '')
    act_time = request.GET.get('time', '')
    act_deadline = request.GET.get('deadline', '')
    act_sponsor = int(request.GET.get('sponsor', ''))
    act_intr = request.GET.get('intr', '')
    act_type = int(request.GET.get('type', ''))
    act_attr = request.GET.get('attr', '')
    act = models.Activity.objects.create(name = act_name, theme = act_theme, location = act_location,\
    time = act_time, deadline = act_deadline, sponsor = act_sponsor, introduction = act_intr,\
    type = act_type, attr = act_attr, complaint_num = 0)
    models.Organize.objects.create(user = act_sponsor, activity = act.id)
    return HttpResponse("OK")


def get_activity(request):
    get_id = int(request.GET.get('id', ''))
    act = models.Activity.objects.get(id = get_id)
    join = models.Join.objects.filter(activity = get_id)
    join_list = []
    for join_item in join:
        join_list.append(join_item.user)
    sign_up = models.Sign_up.objects.filter(activity = get_id)
    sign_up_list = []
    for sign_up_item in sign_up:
        sign_up_list.append(sign_up_item.user)
    comments =  act.comments.all()
    comments_list = []
    for comments_item in comments:
        comments_list.append(comments_item.id)
    ret = {
        'name':act.name,
        'theme':act.theme,
        'location':act.location,
        'time':str(act.time),
        'deadline':str(act.deadline),
        'sponsor':act.sponsor,
        'intr':act.introduction,
        'type':act.type,
        'attr':act.attr,
        'join_list':join_list,
        'sign_up_list':sign_up_list,
        'comments_list':comments_list,
        'complaint_num':act.complaint_num,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

def join_activity(request):
    user_id = int(request.GET.get('userid', ''))
    act_id = int(request.GET.get('actid', ''))
    models.Join.objects.create(user = user_id, activity = act_id)
    return HttpResponse("OK")

def sign_up_activity(request):
    user_id = int(request.GET.get('userid', ''))
    act_id = int(request.GET.get('actid', ''))
    models.Sign_up.objects.create(user = user_id, activity = act_id)
    return HttpResponse("OK")

def search_by_name(request):
    get_name = request.GET.get('name', '')
    act = models.Activity.objects.get(name = get_name)
    get_id = act.id
    join = models.Join.objects.filter(activity = get_id)
    join_list = []
    for join_item in join:
        join_list.append(join_item.user)
    sign_up = models.Sign_up.objects.filter(activity = get_id)
    sign_up_list = []
    for sign_up_item in sign_up:
        sign_up_list.append(sign_up_item.user)
    comments =  act.comments.all()
    comments_list = []
    for comments_item in comments:
        comments_list.append(comments_item.id)
    ret = {
        'name':act.name,
        'theme':act.theme,
        'location':act.location,
        'time':str(act.time),
        'deadline':str(act.deadline),
        'sponsor':act.sponsor,
        'intr':act.introduction,
        'type':act.type,
        'attr':act.attr,
        'join_list':join_list,
        'sign_up_list':sign_up_list,
        'comments_list':comments_list,
        'complaint_num':act.complaint_num,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

def get_act_comments(request):
    act_id = int(request.GET.get('actid', ''))
    act = models.Activity.objects.get(id = act_id)
    all_comments = act.comments.all()
    comment_list = []
    for comments_item in all_comments:
        comment_list.append(comments_item.id)
    ret = {
        'data':comment_list,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

def get_comment_by_id(request):
    comment_id = int(request.GET.get('cmtid', ''))
    comment = models.Comment.objects.get(id = comment_id)
    ret = {
        'time':str(comment.time),
        'text':comment.text,
        'complaint_num':comment.complaint_num,
        'actvity':comment.act_id,
        'user':comment.user_id,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

def get_user_comments(request):
    user_id = int(request.GET.get('userid', ''))
    user = models.User.objects.get(id = user_id)
    all_comments = user.comments.all()
    comment_list = []
    for comments_item in all_comments:
        comment_list.append(comments_item.id)
    ret = {
        'data':comment_list,
    }
    return HttpResponse(json.dumps(ret), content_type='application/json')

def comment(request):
    userid = int(request.GET.get('userid', ''))
    actid = int(request.GET.get('actid', ''))
    comment_text = request.GET.get('comment', '')
    act = models.Activity.objects.get(id = actid)
    user = models.User.objects.get(id = userid)
    new_comment = models.Comment.objects.create(user_id = userid, act_id = actid, text = comment_text, complaint_num = 0)
    act.comments.add(new_comment)
    user.comments.add(new_comment)
    return HttpResponse("OK")


