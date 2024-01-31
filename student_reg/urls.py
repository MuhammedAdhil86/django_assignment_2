from django.urls import path
from .import views
urlpatterns = [
    path('',views.insert,name='register'),
    path('view/',views.view,name='view'),
    path('details/<str:pk>',views.detail,name='details'),
    path('update/<str:pk>',views.update,name='update'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('login/',views.login,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('displ/',views.display,name='displ'),
    path('loglog/',views.loglog,name='loglog'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminwelcom/',views.adminwelcom,name='adminwelcom'),
   
    
]