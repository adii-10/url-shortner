from django.urls import path
from short import views

urlpatterns = [
    path('', views.head, name='head'),
    path('create',views.create,name='create'),
    path('<str:pk>', views.go, name='go')
]