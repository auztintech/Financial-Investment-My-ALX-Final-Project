from django.db import models
from user.models import User
from django.db.models.signals import pre_delete,post_delete,post_save,pre_save,m2m_changed
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from allauth.account.signals import user_signed_up
# Create your models here.

class Referral(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='reffcode')
	sign_up = models.PositiveIntegerField(default=0)#Nos of Signup 
	# no_referals = models.PositiveIntegerField(default=0)#Nos of Signup 
	visit = models.PositiveIntegerField(default=0)#Nos who visited our site using hes link
	# referral_link = models.URLField(blank=True,null=True)
	# paid_count = models.PositiveIntegerField(default=0)
	referral_link = models.CharField(max_length=200,blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True)
	########## CONTROL PAYMENT ###################
	# have_accepted = models.BooleanField(default=False)#True if Once the user have accepted hes pay
	# created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)


##Referral Model that is only created when a user register using ur link
class ReferredUser(models.Model):
	referrer = models.ForeignKey(User,on_delete=models.CASCADE,related_name='referer')#who refer
	referred = models.ForeignKey(User,on_delete=models.CASCADE,related_name='referee')#Person dat is refer
	class Meta:
		unique_together = ['referrer','referred']






'''
I listen for a signup signal from allauth once a user signup i create Referral for he/she, so that
the user can refer others
'''
@receiver(user_signed_up)
def ref_generator(request,user,**kwargs):
	instance = user
	user_id = str(instance.id)
	unique_id = get_random_string(length=30)
	# combine = 'http://127.0.0.1:8000/ref/'+unique_id+user_id
	# combine = 'http://127.0.0.1:8000/ref/'+unique_id+user_id
	combine = user_id+unique_id ##Original
	Referral.objects.create(user=instance,referral_link=combine)
	'''
	Check if they is a ref-code in the session if True we give support to who refer d person
	'''
	if 'ref_code' in request.session:
		ref_code = request.session.get('ref_code')
		person_that_refer = Referral.objects.get(referral_link=ref_code)
		ReferredUser.objects.create(referrer=person_that_refer.user,referred=instance)
		person_that_refer.sign_up +=1
		person_that_refer.save()
	else:
		pass



