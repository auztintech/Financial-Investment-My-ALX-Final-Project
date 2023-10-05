from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Referral,ReferredUser
from user.models import User
# Create your views here.


@login_required
def all_ref(request):
	mauu = request.user

	# man = Referral.objects.filter(user=user)#User he referred
	# man =- Referral.objects.get(user=user)
	man = get_object_or_404(Referral,user=mauu)
	linkaa = man.referral_link
	link = "https://www.auztininvestmentlimited.com/ref/"+linkaa
	request.session['referral_link'] = link
	return render(request,'referral/referal.html',{'man':man,'link':link,})

'''
Checking whether id the user have meet the requirement to be awarded payment
'''
# @login_required
# def bonus(request):
# 	user = request.user
# 	person = get_object_or_404(Referral,user=user)
# 	if person.paid_count >= 5:
# 		person.paid_count -=5
# 		# person.can_now_accept = True
# 		person.save()
# 		involve = get_object_or_404(User,id=user.id)
# 		involve.bonus_earner = True #This will b turn to flase once d user have b match
# 		involve.save()
# 		info = "You Have Been Match Please Wait For The Payment Proof "
# 	else:
# 		info = "Refer upto 5 persons and you will be match "
# 	return render(request,'referral/bonus.html',{'info':info,})

