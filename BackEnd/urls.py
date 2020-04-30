from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^new_user/', views.new_user),
    url(r'^authentication/', views.authentication),
    url(r'^get_my_activities/', views.get_my_activities),
    url(r'^get_all_activities/', views.get_all_activities),
    url(r'^get_joined_activities/', views.get_joined_activities),
    url(r'^get_signed_up_activities/', views.get_signed_up_activities),
    url(r'^get_activity/', views.get_activity),
    url(r'^new_activity/', views.new_activity),
    url(r'^join_activity/', views.join_activity),
    url(r'^sign_up_activity/', views.sign_up_activity),
    url(r'^search_by_name/', views.search_by_name),
    url(r'^get_comment_by_id/', views.get_comment_by_id),
    url(r'^get_user_comments/', views.get_user_comments),
    url(r'^get_act_comments/', views.get_act_comments),
    url(r'^comment/', views.comment),
]