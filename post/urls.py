from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url(r'page/(\d+)/',views.index),
    url(r'post/(\d+)',views.detail),
    url(r'aboutme',views.aboutme),
    url(r'category/(\d+)/', views.category),
    url(r'^archive/(\d{4})/(\d{1,2})/$',views.archive),
    url(r'^archive/$',views.archive),



]