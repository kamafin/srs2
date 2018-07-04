from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='student_home'),
    url(r'^list_json/$', views.student_list_json.as_view(), name="student_list_json"), #utk papar list student bila guna url .../list_json
    url(r'^home/$',views.home_json,name='student_home_json'),   #utk papar page home
    url(r'^sbadmin/$',views.home_sbadmin,name='student_home_sbadmin'),   #utk papar page sbadmin
    url(r'^(?P<pk>\d+)/$', views.student_detail, name='student_detail'),   #utk papar student detail
    url(r'^new/$',views.student_new, name='student_new'), 
    url(r'^(?P<pk>\d+)/remove$', views.student_remove, name='student_remove'),
    url(r'^(?P<pk>\d+)/edit$', views.student_edit, name='student_edit'),
]