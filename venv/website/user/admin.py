from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,Help_desk
from wallet.models import Withdraw, Earned, Deposit
from .models import KYCApplication,UserProfile


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['username', 'email','date_joined']
    # list_editable = ['verification', 'account_balance',]
    ordering = ['-date_joined',]
    fieldsets = UserAdmin.fieldsets + (
            ('Account Informations', {'fields': ('payment_option','payment_address',)}),
            ('Wallet Details', {'fields': ('last_deposit', 'total_deposit', 'balance','profit')}),
            ('Pakage Details', {'fields': ('total_packages','bonus','active_packages','ref_bonus')}),
            
    )
admin.site.register(User, UserAdmin)


admin.site.register(Help_desk)

class KYCApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'identification_doc', 'address_doc', 'id_card_or_passport', 'proof_of_address')
    list_filter = ('identification_doc', 'address_doc')
    search_fields = ('id', 'identification_doc', 'address_doc')
    list_per_page = 20

admin.site.register(KYCApplication, KYCApplicationAdmin)



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','profile_picture']
    list_editable = ['profile_picture']