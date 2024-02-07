from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    income = models.FloatField()

class Expense_category(models.Model):
    name = models.CharField(primary_key=True,maxlength=30)
    if_essential = models.BooleanField(default=False)

class Expense(models.Model):
    category = models.ForeignKey(Expense_category,on_delete=models.CASCADE,null=False)
    fk_user_id1 = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=False)
    amount = models.FloatField()
    time = models.DateTimeField()
    desc = models.TextField(null=True)

class Analysis(models.Model):
    fk_user_id2 = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=False)
    avg_daily = models.FloatField()
    avg_monthly = models.FloatField()
    avg_annual = models.FloatField()
    totalEssentialExpenditure = models.FloatField()
    goal_savings = models.FloatField()
    non_ess_limit = models.FloatField()