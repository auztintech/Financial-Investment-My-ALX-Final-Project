from django import forms
from .models import Deposit, Withdraw, MakeDeposit




class MakeDepositForm(forms.ModelForm):
	class Meta:
		model = MakeDeposit
		fields = ('payment_proof','payment_option')


class DepositForm(forms.ModelForm):
	class Meta:
		model = Deposit
		fields = ('amount',)



class WithdrawForm(forms.ModelForm):
	class Meta:
		model = Withdraw
		fields = ('amount',)