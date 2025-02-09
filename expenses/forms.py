from django import forms
from .models import Transactions, Category

class TransactionsCreateForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = "__all__"

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name")