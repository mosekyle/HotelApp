"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name= 'index'),
    path('room/', views.room, name= 'room'),
    path('services/', views.service, name= 'services'),
    path('team/', views.team, name= 'team'),
    path('testimonial/', views.testimonial, name= 'testimonial'),
    path('booking', views.booking, name= 'booking'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),
    path('contact/', views.contact, name='contact'),
    path('book/', views.global_booking, name='global_booking'),
    path('receipt/<int:booking_id>/', views.booking_receipt, name='booking_receipt'),
]


