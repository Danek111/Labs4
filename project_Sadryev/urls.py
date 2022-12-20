from django.urls import path,include
from Sadryev import views
from User import views as user_views
urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    path("edit/<int:pk>/", views.edit),
    path("delete/<int:pk>/", views.delete),
    path('accounts/', include('User.urls')),
    path('register/', user_views.register, name='register'),
]
