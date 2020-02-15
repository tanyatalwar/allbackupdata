from django.conf.urls import url
from first_app import views

urlpatterns =[
 url('home/',views.index,name='index'),
 url('user/',views.users,name='users'),
 url('form/',views.users,name='form_name_view'),
 url('base/',views.base,name='base'),
 url('other/',views.other,name='other'),
]
