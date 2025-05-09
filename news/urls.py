from django.urls import path 
from .views import homepage,detail,category_funk

urlpatterns=[
    path('',homepage,name='home'),
    path('news/<int:id>/',detail,name='detail'),
    path('category/<int:id>/',category_funk,name='category')
]