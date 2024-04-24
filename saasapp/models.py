from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import datetime

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # Other fields for tenant details

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()
    duration_months = models.IntegerField()
    trial_days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Other fields for plan details

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    subscription_start_date = models.DateTimeField(null=True, blank=True)
    subscription_end_date = models.DateTimeField(null=True, blank=True)
    is_subscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Other user profile fields

class Payment(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    # Other payment details

class PaymentGateway(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)