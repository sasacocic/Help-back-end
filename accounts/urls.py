from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.Accounts_List.as_view()),
]
