from . import views
from django.urls import path


from django.conf import settings
urlpatterns = [

    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='add'),
    # path('contact/',views.contact,name='contact')


]