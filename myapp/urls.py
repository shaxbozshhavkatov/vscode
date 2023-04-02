from django.urls import path
from .views import *


urlpatterns = [
    path('blog/',HomePage,name = "home"),
    path('detail/<str:name>',aboutpage,name = 'detail')
]