from django.urls import path
from . import views

urlpatterns = [
	path('', views.getRoutes, name="routes"),
	path('notes/', views.getNotes, name="notes"),
	path('notes/creation/', views.createNote, name="createNote"),
	path('notes/<str:pk>/updation/', views.updateNote, name="updateNote"),
	path('notes/<str:pk>/deletion/', views.deleteNote, name="deleteNote"),
	path('notes/<str:pk>/', views.getNote, name="note"),
]