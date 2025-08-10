from django.contrib import admin

from expenses.models import Transactions, Category

# Register your models here.
admin.site.register(Transactions)
admin.site.register(Category)
