from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('leave_management/',views.leave_management),
    path('login/',views.login),

]