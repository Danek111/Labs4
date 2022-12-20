from django.urls import path,include
from Sadryev import views
 
urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
    path('accounts/', include('User.urls')),
]