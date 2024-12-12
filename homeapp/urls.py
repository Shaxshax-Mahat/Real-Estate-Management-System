from django.contrib import admin
from django.urls import path
from homeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('agents/', views.agents, name='agents'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.properties, name='properties'),
    path('property_single/', views.property_single, name='property-single'),
    path('service_details/', views.service_details, name='service-details'),
    path('services/', views.services, name='services'),
    path('starter_page/', views.starter_page, name='starter-page'),
    path('show_contact/', views.show_contact, name='show-contact'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),

    #Mpesa API urls
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
