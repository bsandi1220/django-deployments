from django.conf.urls import url
from myApp import views


#template tagging

app_name = 'myApp'

urlpatterns = [
    url(r'^relative/$',views.relative, name='relative'),
    url(r'^other/$',views.other, name='other'),

]
