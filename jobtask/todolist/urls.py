
from django.urls import path

from .views import defaultview,TodoCreate,TodoList1,TodoUpdate,TodoDelete
app_name = "todolist"
urlpatterns = [
    path('',defaultview,),
    path('create/',TodoCreate.as_view(),name='create'),
    path('list/',TodoList1.as_view(),name="list"),
    path('delete/<int:pk>',TodoDelete.as_view(),name="delete"),
    path('update/<int:pk>',TodoUpdate.as_view(),name="update"),

]