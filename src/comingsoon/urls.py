from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /comingsoon/
    url(r'^$', views.InterestedUserCreate.as_view(), name='index'),
]
