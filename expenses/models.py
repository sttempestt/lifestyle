from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class Transactions(models.Model):
    R = 'R'
    S = 'S'
    types = [
        (R, 'received'),
        (S, 'spent'),
    ]
    E = 'E'
    C = 'C'
    P = 'P'
    statuses = [
        (E, 'expected'),
        (C, 'completed'),
        (P, 'pending'),
    ]
    description = models.CharField(max_length=50, default="", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.CharField(choices=types, max_length=1)
    date_completed = models.DateTimeField(default=timezone.now, blank=True)
    date_created = models.DateTimeField(null=True)
    date_expected = models.DateTimeField(null=True)
    status = models.CharField(choices=statuses, max_length=1, default=C, blank=True)
    def __str__(self):
        formatted_date = self.date_completed.strftime("%Y-%m-%d %H:%M")  
        account_display = self.get_account_display()
        if self.status == 'C':
            return f"{formatted_date}: {self.sum} {account_display}, {self.description}"
        else:
            return f"{self.status} {formatted_date}: {self.sum} {account_display}, {self.description}"
        

#bob