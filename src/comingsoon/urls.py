from django.conf.urls import url
from django.shortcuts import redirect
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # ex: /comingsoon/
    url(r'^$', views.InterestedUserCreate.as_view(), name='index'),
    # ex: /comingsoon/thanks/
    url(r'^thanks/$', TemplateView.as_view(template_name="comingsoon/thanks.html"), name='thanks'),
]
