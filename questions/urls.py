from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.new_questions, name='new_questions'),
    url(r'^hot$', views.hot_questions, name='hot_questions'),
    url(r'^tag/*$', views.find_by_tag, name='find_by_tag'),
    url(r'^question/*$', views.question, name='question'),
    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^ask$', views.ask, name='ask'),
    url(r'^settings$', views.settings, name='settings')
]
