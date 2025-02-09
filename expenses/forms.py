from django import forms
from .models import Transactions, Category

class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
