from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^sign_log/$',views.sign_log,name='sign_log'),
    url(r'^account_create/$',views.account_create,name='account_create'),
]
