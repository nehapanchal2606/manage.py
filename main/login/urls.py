from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('show/', views.view),
    path('home/', views.home),
    path('register/', views.register),
    path('insert/', views.insert),
    path('blog/', views.blog_show),
    path('blog_details/<int:id>', views.blog_details),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('logout/', views.logout),
    path('test/', views.test),


]








