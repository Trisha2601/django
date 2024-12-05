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
from django.urls import path
from App.views import * 
from App.views import students_list
#from .views import StudentList, GetView, PutView, PatchView, DeleteView, StudentContactInfoListCreateView, StudentContactInfoDetailView
#from django.shortcuts import redirect

urlpatterns = [
    #path('',home,name='home'),
    # path('add/student-list/', StudentList.as_view(), name='student-list'),
    path('post/', StudentList.as_view()),
    #path('', lambda request: redirect('get/')),# Example for home URL
    path('get/', GetView.as_view()),  # Add more paths as needed
    # path('patch/', StudentList.as_view(), name='patch'),
    path('del/<int:id>', DeleteView.as_view()),
    path('put/<int:id>', PutView.as_view()),
    path('patch/<int:id>',PatchView.as_view()),
    path('contact/delete/<int:contact_id>/', ContactInfoDelete.as_view(), name='contact-info-delete'),
     path('contact/', StudentContactInfoListCreate.as_view(), name='contact-list-create'),
    path('contact/<int:id>/',StudentContactInfoDetail.as_view(), name='contact-detail'),
    path('get/', get_all_students_and_contact_info, name='get_students_and_contact_info'),
    path('students/',get_all_students_and_contact_info, name='students_list'),
    path('students/', students_list, name='students_list'),
]