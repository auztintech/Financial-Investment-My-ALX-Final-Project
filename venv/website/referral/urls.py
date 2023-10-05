from django.urls import path
from . import views



app_name = "referral"

urlpatterns = [
	path('all_ref/', views.all_ref, name='all_ref'),
	
]
