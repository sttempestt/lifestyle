from django.db import models
from django.utils import timezone

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, default="", blank=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self):
        return f"{self.name}"


class Transactions(models.Model):
    R = "R"
    S = "S"
    types = [
        (R, "received"),
        (S, "spent"),
    ]
    E = "E"
    C = "C"
    P = "P"
    statuses = [
        (E, "expected"),
        (C, "completed"),
        (P, "pending"),
    ]
    description = models.CharField(max_length=50, default="", blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.CharField(choices=types, max_length=1)
    date_completed = models.DateTimeField(default=timezone.now, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_expected = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=statuses, max_length=1, default=C, blank=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="transactions"
    )

    def __str__(self):
        formatted_date = self.date_completed.strftime("%Y-%m-%d %H:%M")
        account_display = self.get_account_display()
        if self.status == "C":
            return f"{formatted_date}: {self.sum} {account_display}, {self.description}"
        else:
            return f"{self.status} {formatted_date}: {self.sum} {account_display}, {self.description}"
        
    def calculate_balance(self):
        balance = 0
        for transaction in Transactions:
            if transaction.status == 'C':
                if transaction.account == 'R':
                    balance += transaction.sum
                if transaction.account == 'S':
                    balance -= transaction.sum
        return balance
