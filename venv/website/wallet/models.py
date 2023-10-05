from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.conf import settings
import datetime
from django.utils import timezone
import random 
from easy_thumbnails.fields import ThumbnailerImageField
import string
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from user.models import User
import django

#plan model, the admin creates plans dynamically from the admin pade

class Plan(models.Model):
    plan_name = models.CharField(max_length=30,unique=True)
    percentage = models.PositiveIntegerField()
    plan_duration = models.PositiveIntegerField(help_text="Duration in days ")
    min_deposit = models.DecimalField(max_digits=20, decimal_places=2)
    max_deposit = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_name

    class Meta:
        ordering = ('created',)


#manually depositing funds without following any particular plan
class MakeDeposit(models.Model):
    PAYMENT_OPTION = (
        ('Bank Transfer', 'Bank Transfer'),
        ('Ethereum', 'Ethereum'),
        ('Bitcoin', 'Bitcoin'),
        ('Credit Card', 'Credit Card'),
    )

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
        related_name='user_make_deposit')
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    payment_proof = ThumbnailerImageField(upload_to='payment_proof',null=True, blank=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='Pending')
    payment_option = models.CharField(max_length=20,choices=PAYMENT_OPTION, default='Bank Transfer')
    deposit_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('-deposit_date',)



#depositing using a plan
class Deposit(models.Model):
    STATUS_CHOICES = (
        ('Unverify', 'Unverify'),
        ('Verified', 'Verified'),
    )

    PAID_STATUS = (
        ('Not Paid', 'Not Paid'),
        ('Paid', 'Paid'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
        related_name='user_deposit')
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE,related_name='user_plan')
    transaction_ID = models.CharField(max_length=400,default="")
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAID_STATUS, default='Not Paid')#Control by user
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='Unverify')#Verify by admin
    active = models.BooleanField(default=False)#Used durin cron to know if he's got its roi or not
    start_counting_date = models.DateTimeField(blank=True,null=True)
    deposit_date = models.DateTimeField(default=django.utils.timezone.now)
    # deposit_date = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ('-updated',)



#this is model for withdrawing funds that are due
class Withdraw(models.Model):
    STATUS_CHOICES = (
        ('Processing', 'Processing'),
        ('Paid', 'Paid'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
        related_name='user_withdraw')
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='Processing')
    withdraw_date = models.DateTimeField(default=django.utils.timezone.now)
    # withdraw_date = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.user.username

    class Meta:
        ordering = ('-updated',)

#this is the money earned by the investor, 
class Earned(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
        related_name='user_earned')
    amount_invested = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    profit_gained = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    earned_date = models.DateTimeField(default=django.utils.timezone.now)
    # earned_date = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.user.username

    class Meta:
        ordering = ('-updated',)





class Company_Account(models.Model):
    account_number = models.CharField(max_length=30)
    account_name = models.CharField(max_length=50)
    bank = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.account_name


    class Meta:
        ordering = ('-updated',)



########################### SIGNALS SIGNALS SIGNALS SIGNALS ####################################### 


#signals that will send emails will be written under here