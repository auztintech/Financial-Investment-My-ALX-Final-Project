from django.shortcuts import render,redirect,get_object_or_404
from wallet.models import Plan
from referral.models import Referral




'''
This view controls the referral links, that is any link that have strings after the main url,
and we try to get the user that have the link
'''
def RefLink(request,ref):
	# user_having_ref = get_object_or_404(Referral,referral_link=ref)
	try:
		# user = Referral.objects.get(referral_link=ref)
		user = get_object_or_404(Referral,referral_link=ref)
		request.session['ref_code']=user.referral_link#Put the user in acceser browser session
		user.visit +=1 #Increment the value
		user.save() #update the user(i.e save it to the data base)
	except Referral.DoesNotExist:
	# except user_having_ref.DoesNotExist:
		pass
	# return redirect('home:home_page')
	return redirect('account_signup')



def plan_page(request):
	context = {}
	page_title = "Plans"
	plans = Plan.objects.all()
	context['page_title'] = page_title
	context['plans'] = plans
	return render(request, 'pages/plan_page.html',context)

def home_page(request):
	context = {}
	page_title = "Home"
	plans = Plan.objects.all()
	context['page_title'] = page_title
	context['plans'] = plans
	# return render(request, 'pages/warning.html',context)
	return render(request, 'pages/home_page3.html',context)


def about_page(request):
	page_title = "About Us"
	context = {'page_title':page_title}
	return render(request, 'pages/about_page.html',context)


def contact_page(request):
	page_title = "Contact Us"
	context = {'page_title':page_title}
	return render(request, 'pages/contact_page.html',context)



def terms_page(request):
	page_title = "Terms and Conditions"
	context = {'page_title':page_title}
	return render(request, 'pages/terms_page.html',context)



def privacy_page(request):
	page_title = "Privacy Policy"
	context = {'page_title':page_title}
	return render(request, 'pages/privacy_page.html',context)



def faq_page(request):
	page_title = "FAQ"
	context = {'page_title':page_title}
	return render(request, 'pages/faq_page.html',context)