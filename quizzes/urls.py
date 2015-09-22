from django.conf.urls import url
from . import views

#Acces to this routes using /quizzes/urlpattern
urlpatterns = [
    #List decks
    url(r'^list/$', views.index, name='index'),
    #Do a quiz
    url(r'^detail/(?P<deck_name>.+)/$', views.detail, name='detail'),
    #See results
    url(r'^results/(?P<deck_name>.+)/$', views.results, name='results'),
    #Save a result
    url(r'^save/$', views.save, name='save'),
]