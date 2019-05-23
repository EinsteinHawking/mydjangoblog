from django.urls import path

from . import views

urlpatterns = [
    path('',views.test1),
    path('main/', views.test2,name="test"),
    path('test/', views.test3),


    path('ajax/index/',views.ajax_index),
    path('ajax/get/', views.ajax_get),
    path('ajax/post/', views.ajax_post),
    path('ajax/json/', views.ajax_json),
]
