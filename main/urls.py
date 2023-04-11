from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('details/<str:id>' , views.details , name='detailed'),
    path('createTodo', views.createTodo, name='createTodo'),
    path('createTodoItem' , views.createTodoItem ,name='createTodoItem'),
    path('deleteTodoItem/<str:pk>' , views.deleteTodoItem ,name='deleteTodoItem'),
    path('updateTodoItem/<str:pk>' , views.updateTodoItem ,name='updateTodoItem'),
    path('signup', views.createUser , name='signup'),
    path('login', views.loginUser , name='login'),
    path('logout', views.logoutUser , name='logout'),
]