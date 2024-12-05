# """
# URL configuration for Project project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path,include
# from App.views import *


# urlpatterns = [
#     path('admin/', admin.site.urls),#12345
#     #path('add/', StudentList.as_view(),),
#     path('get/',Getview.as_view()),
#     path('put/',PutView.as_view()),
#     path('patch/',PatchView.as_view()),
#     path('del/<int:id>',Deleteview.as_view()),
#     #path('',StudentList.as_view(),name='home')
#     #path('api/', include('App.urls')),
# ]
from django.urls import path,include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('App.urls')),
]
    
    # path('add/student-list/', StudentList.as_view(), name='student-list'),
    # path('', StudentList.as_view(), name='home'),  # Example for home URL
    # path('put/', StudentList.as_view(), name='put'),  # Add more paths as needed
    # path('patch/', StudentList.as_view(), name='patch'),
    # path('del/', StudentList.as_view(), name='delete'),
