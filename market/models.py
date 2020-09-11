from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})
    
def get_bank():
    return User.objects.filter(username='Bank_of_Beehive').first()

class Transaction(models.Model):
    DIRECTION_CHOICES = [
        ('Recieving', 'Recieving Bee Bonds'),
        ('Spending', 'Spending Bee Bonds')
    ]
    direction = models.CharField(max_length=25, choices=DIRECTION_CHOICES, default='Spending')
    value = models.BigIntegerField(help_text="Value of transaction in ISK/Bee Bonds")
    description = models.CharField(max_length=100, help_text="Deposit, Withdrawal, Exchange, ect.")
    details = models.TextField(blank=True, help_text="List of items, details of transaction. Please provide prices where possible.")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, default=get_bank, related_name='+')
    date = models.DateTimeField(default=timezone.now)
    authorised = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('market-transactions')