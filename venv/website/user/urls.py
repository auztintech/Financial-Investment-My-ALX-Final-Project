from django.urls import path
from . import views



app_name = "user"

urlpatterns = [
	path('dashboard/', views.dashboard, name='dashboard'),
	path('profile/', views.profile, name='profile'),
	path('profile_2/', views.profile_2, name='profile_2'),
	path('increase_amount/', views.increase_amount, name='increase_amount'),
	path('create_ticket/', views.create_ticket, name='create_ticket'),
	path('kyc_apply/', views.kyc_apply, name='kyc_apply'),
	path('success_page/', views.success_page, name='success_page'),
	path('profile_picture_upload/', views.profile_picture_upload, name='profile_picture_upload'),
	# path('contact-us/', views.contact_page, name='contact_page'),
	# path('terms-conditions/', views.terms_page, name='terms_page'),
	# path('privacy-policy/', views.privacy_page, name='privacy_page'),
]
