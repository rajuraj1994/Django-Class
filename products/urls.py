from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('test/',views.testFunc),
    path('addproduct/',views.post_product),
    path('addcategory/',views.post_category)
]