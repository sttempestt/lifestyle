from django import forms
from .models import Transactions, Category


class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [
            "description",
            "category",
            "sum",
            "account",
            "date_completed",
            "date_created",
            "date_expected",
            "status",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "icon"]
