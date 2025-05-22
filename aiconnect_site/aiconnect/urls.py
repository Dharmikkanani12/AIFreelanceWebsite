"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_view, name='projects'),
    path('developers/', views.developers_view, name='developers'),
    path('postproject/', views.postproject_view, name='postproject'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]