
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models.signals import pre_delete,post_delete,post_save,pre_save,m2m_changed
from django.dispatch import receiver
from django.conf import settings
from django.utils.crypto import get_random_string
from allauth.account.signals import user_signed_up
from django.core.mail import send_mail
from easy_thumbnails.fields import ThumbnailerImageField

#my user model extending the django's AbstractUser 

class User(AbstractUser):
    ACCOUNT_CHOICES = (
    	("bitcoin address","bitcoin address"),
    	("perfect money account","perfect money account"),
    )
    payment_option = models.CharField(max_length=30,choices=ACCOUNT_CHOICES,blank=True)
    payment_address = models.CharField(max_length=300,blank=True)
    account_number = models.CharField(max_length=15, blank=True)
    account_name = models.CharField(max_length=255, blank=True)
    bank_name = models.CharField(max_length=100, blank=True)
    ############################### WALLET DETAILS #####################
    last_deposit = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    total_deposit = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    balance = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    profit = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    bonus = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    active_packages = models.PositiveIntegerField(default=0)
    total_packages = models.PositiveIntegerField(default=0)
    ref_bonus = models.DecimalField(max_digits=20, decimal_places=2,default=10.00)
    last_withdrawal = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    pending_withdrawal = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    total_withdraw = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    total_earned = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)

    class Meta:
    	ordering = ('-date_joined',)

# user can upload his/her image as profile picture
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/',
     default="no-picture.png")





#this is Know Your Customer , the user uploads three documents the affirms his claims of identity
class KYCApplication(models.Model):
    identification_doc_choices = (
        ('ID', 'National ID'),
        ('passport', 'International passport'),
    )
    address_doc_choices = (
        ('utility_bill', 'Utility Bill'),
        ('bank_reference', 'Bank Reference'),
        ('proof_of_residence', 'Proof of Residence'),
        ('driver_or_residence_permit', 'Driver or Residence Permit'),
        ('other', 'Other'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    	related_name='KYCVerification')
    id_card_or_passport = models.ImageField(upload_to='kyc/idimg/', blank=True, null=True)
    proof_of_address = models.ImageField(upload_to='kyc/addressimg/', blank=True, null=True)
    identification_doc = models.CharField(max_length=50, choices=identification_doc_choices)
    address_doc = models.CharField(max_length=50, choices=address_doc_choices)
    def __str__(self):
        return self.user.username


#Help desk is a place within the user's dashboard that he can reach out to the admin or the customer care by 
#by creating tickets stating the kind of support he wants
class Help_desk(models.Model):
    CATEGORY_CHOICES = (
        ('Deposit', 'Deposit'),
        ('Withdrawal', 'Withdrawal'),
        ('Earning', 'Earning'),
        ('Referral', 'Referral'),
        ('Account', 'Account'),
        ('Other', 'Other'),
    )

    TICKET_STATUS = (
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
    )

    PRIORITY_STATUS = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    	related_name='ticket')
    subject = models.CharField(max_length=400)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    priority = models.CharField(max_length=400, choices=PRIORITY_STATUS, default="Low")
    status = models.CharField(max_length=20,choices=TICKET_STATUS, default='Pending')
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('-created',)









