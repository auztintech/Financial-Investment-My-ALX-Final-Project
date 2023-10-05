from django.urls import path
from . import views



app_name = "pages"

urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('ref/<str:ref>/', views.RefLink, name='RefLink'),
	path('plans/', views.plan_page, name='plan_page'),
	path('about-us/', views.about_page, name='about_page'),
	path('faq_page/', views.faq_page, name='faq_page'),
	path('contact-us/', views.contact_page, name='contact_page'),
	path('terms-conditions/', views.terms_page, name='terms_page'),
	path('privacy-policy/', views.privacy_page, name='privacy_page'),
]
