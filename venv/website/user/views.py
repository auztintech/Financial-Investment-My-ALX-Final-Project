from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditProfileForm, HelpDeskForm
from referral.models import Referral,ReferredUser
from user.models import User,Help_desk
# Create your views here.
from wallet.models import Plan, Deposit,Company_Account
from .forms import KYCApplicationForm
from django.utils import timezone
from decimal import Decimal
from . models import UserProfile
from . forms import UserProfileForm


#this is user's dashboard, it is where he is directed to upon signup
@login_required
def dashboard(request):
	context = {}
	user = request.user
	user_referral = get_object_or_404(Referral,user=user)
	company_account = Company_Account.objects.last()
	context['company_account'] = company_account
	linkaa = user_referral.referral_link
	link = "https://www.website.com/ref/"+linkaa
	page_title = "Dashboard"
	context['page_title'] = page_title
	context['user_referral'] = user_referral
	context['link'] = link
	return render(request, 'user/dashboard2.html',context)

#this is the function that allows a user to edit and save his profile details
@login_required
def profile(request):
	context = {}
	page_title = "Profile"
	user = request.user
	context['page_title'] = page_title
	context['user'] = user
	referral_link = request.session.get('referral_link', None)
	if request.method == 'POST':
		form = EditProfileForm(instance=user, data=request.POST)
		if form.is_valid():
			updated_form = form.save(commit=False)
			updated_form.save()
			messages.success(request, "Profile Updated Successfully")
			return redirect("user:profile")
	else:
		form = EditProfileForm(instance=user)
	context['form'] = form
	return render(request, 'user/profile.html',context)

@login_required
def profile_2(request):
	context = {}
	page_title = "Profile"
	user = request.user
	context['page_title'] = page_title
	context['user'] = user
	user_profile_id = request.session.get('user_profile_id')
	context['user_profile_id'] = user_profile_id
	referral_link = request.session.get('referral_link', None)
	if request.method == 'POST':
		form = EditProfileForm(instance=user, data=request.POST)
		if form.is_valid():
			updated_form = form.save(commit=False)
			updated_form.save()
			messages.success(request, "Profile Updated Successfully")
			return redirect("user:profile_2")
	else:
		form = EditProfileForm(instance=user)
	context['form'] = form
	return render(request, 'user/profile2.html',context)


#the function that handles the submission of the ticket
def create_ticket(request):
    if request.method == 'POST':
        form = HelpDeskForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new Help_desk object
            ticket = form.save(commit=False)
            ticket.user = request.user  # Assign the current user
            ticket.save()
            return redirect('user:create_ticket')  # Redirect to a success page
    else:
        form = HelpDeskForm()
    
    return render(request, 'user/help.html', {'form': form})


#the function that handles the submission of the KYC
def kyc_apply(request):
    if request.method == 'POST':
        form = KYCApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or perform any other necessary action
            return redirect('user:success_page')
    else:
        form = KYCApplicationForm()

    return render(request, 'user/kyc_application.html', {'form': form})

def success_page(request):
	context = {}
	return render(request, 'user/success_page.html', context)

#profile picture upload
def profile_picture_upload(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=user_profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            request.session['user_profile_id'] = user_profile
            return redirect('user:profile_picture_upload')  # Redirect to the dashboard
    context = {'form': form, 'user_profile': user_profile}
    return render(request, 'user/profile_upload.html', context)


#this function calculates the return on investment base on the plan chosen by the investor and the percentage rate
def increase_amount(request):
    context = {}
    for deposit in Deposit.objects.filter(active=True):
    	# if timezone.now() >= (deposit.start_counting_date+timezone.timedelta(days=deposit.plan.plan_duration)):
    	if timezone.now() >= (deposit.start_counting_date+timezone.timedelta(minutes=deposit.plan.plan_duration)):
    		percentage = Decimal(deposit.plan.percentage) / Decimal(100)
    		increment = percentage * deposit.amount
    		user = User.objects.get(id=deposit.user.id)
    		###### CAN BE UPDATED
    		user.balance += increment
    		user.profit += increment
    		user.total_earned += increment
    		user.save()
    		deposit.active = False
    		deposit.save()

    return render(request, 'user/increase_amount.html', context)











# def increase_amount(request):
#     context = {}
#     for deposit in Deposit.objects.filter(active=True):
#     	# if timezone.now() >= (deposit.start_counting_date+timezone.timedelta(days=deposit.plan.plan_duration)):
#     	if timezone.now() >= (deposit.start_counting_date+timezone.timedelta(minutes=deposit.plan.plan_duration)):
#     		increment = (deposit.plan.percentage/100)*deposit.amount
#     		user = User.objects.get(id=deposit.user.id)
#     		###### CAN BE UPDATED
#     		user.balance += increment
#     		user.profit += increment
#     		user.total_earned += increment
#     		user.save()
#     		deposit.active = False
#     		deposit.save()

#     return render(request, 'user/increase_amount.html', context)