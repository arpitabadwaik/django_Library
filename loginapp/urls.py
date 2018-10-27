from django.conf.urls import url

from loginapp import views

urlpatterns = [
    url(r'^$', views.load_landing_page, name='load_landing_page')
]
