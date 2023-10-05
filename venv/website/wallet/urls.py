from django.urls import path
from . import views



app_name = "wallet"

urlpatterns = [
	path('make_deposit/', views.make_deposit, name='make_deposit'),
	path('payment_proof/', views.payment_proof, name='payment_proof'),#New
	path('make_deposit/<str:plan_name>/', views.make_deposit_detail, name='make_deposit_detail'),
	path('your_deposit', views.your_deposit, name='your_deposit'),
	path('deposit_authorization/', views.deposit_authorization, name='deposit_authorization'),
	path('ask_for_withdraw/', views.ask_for_withdraw, name='ask_for_withdraw'),
	path('deposit_history/', views.deposit_history, name='deposit_history'),
	path('earning_history/', views.earning_history, name='earning_history'),
	path('withdraw_history/', views.withdraw_history, name='withdraw_history'),
	path('about_to_withdraw/', views.about_to_withdraw, name='about_to_withdraw'),
]
