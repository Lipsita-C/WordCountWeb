from django.contrib import admin
from django.urls import path 
from home import views





urlpatterns = [
    path('upload_resume/',views.upload_resume, name = "files" ),
    
]



admin.site.site_header = "Lipsita World Admin"
admin.site.index_title = "Welcome to Lipsita World"
admin.site.site_title = "Lipsita Choudhuy"

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("service", views.service, name='service'),
    path("contact", views.contact, name='contact'), 
    

    
]

