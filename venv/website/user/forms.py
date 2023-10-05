from .models import User,Help_desk, KYCApplication,UserProfile
from allauth.account.forms import SignupForm
from django import forms
from django.shortcuts import get_object_or_404

#this is the user's signup form
class MyCustomSignupForm(SignupForm):
	ACCOUNT_CHOICES = (
		("bitcoin address","bitcoin address"),
		("perfect money account","perfect money account"),
	)
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	def save(self, request):
		data = self.cleaned_data
		user = super(MyCustomSignupForm, self).save(request)
		user_profile = get_object_or_404(User,id=user.id)
		user_profile.first_name = data['first_name']
		user_profile.last_name = data['last_name']
		user_profile.save()
		return user

#this is the user's edit profile form, he can edit username, payment_addre
class EditProfileForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','payment_address','email', 'account_number', 'account_name', 'bank_name')



#this is the form to create ticket if a user has any complain
class HelpDeskForm(forms.ModelForm):
    class Meta:
        model = Help_desk
        fields = ['subject', 'category', 'priority', 'message']
        # You can customize the widgets and labels for the form fields if needed.
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'subject': 'Subject',
            'category': 'Category',
            'priority': 'Priority',
            'message': 'Message',
        }

#the know your customer form
class KYCApplicationForm(forms.ModelForm):
	class Meta:
		model = KYCApplication
		fields = ['identification_doc', 'id_card_or_passport', 'address_doc', 'proof_of_address']


#the form for a user to upload a profile picture
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
