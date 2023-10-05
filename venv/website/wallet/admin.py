from django.contrib import admin

# Register your models here.
from .models import Plan,Withdraw, Earned, Deposit, MakeDeposit, Company_Account



@admin.register(MakeDeposit)
class MakeDepositAdmin(admin.ModelAdmin):
	list_display = ['user','amount','status','payment_option','deposit_date']
	list_editable = ['status','amount']


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
	list_display = ['user','amount','status','deposit_date']
	list_editable = ['status','amount']



@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
	list_display = ['plan_name','percentage','plan_duration','min_deposit','max_deposit','created']
	list_editable = ['min_deposit','max_deposit']

# @admin.register(Deposit)
# class DepositAdmin(admin.ModelAdmin):
# 	list_display = ['user','plan','amount','payment_status','active','deposit_date']



@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
	list_display = ['user','amount','status','withdraw_date','created']



@admin.register(Earned)
class EarnedAdmin(admin.ModelAdmin):
	list_display = ['user','amount_invested','profit_gained','earned_date','created']

@admin.register(Company_Account)
class Company_AccountAdmin(admin.ModelAdmin):
	list_display = ['account_number', 'account_name', 'bank']