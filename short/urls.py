from django.urls import path
from short import views

urlpatterns = [
    path('', views.head, name='head'),
    path('create',views.create,name='create'),
    path('favicon.ico', views.favicon_view),
    path('<str:pk>', views.go, name='go')
]
