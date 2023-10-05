from django.contrib import admin
from .models import Referral,ReferredUser

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
	list_display = ('user','visit','sign_up', 'referral_link','created', )
	# list_editable = ['no','account_name']



@admin.register(ReferredUser)
class ReferredUserAdmin(admin.ModelAdmin):
	list_display = ('referrer','referred',)