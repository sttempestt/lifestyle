from django.shortcuts import render
from .models import Transactions, Category
from .forms import  TransactionsForm, CategoryForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def HomeView(TemplateView):
    template_name = 'expenses/home.html'
    def get_context_data(self):
        context = super().get_context_data()
        context["transactions"] = Transactions.objects.all()
        return context
    
class TransactionsView(ListView):
    template_name = 'expenses/transactions_list.html'
    model = Transactions

class CreateTransactionView(CreateView):
    template_name = 'expenses/create_transaction.html'
    model = Transactions

class UpdateTransactionView(UpdateView):
  template_name = 'expenses/edit_transaction.html'
  model = Transactions
  form_class = TransactionsForm

class DeleteTransactionView(DeleteView):
  template_name = 'expenses/delete_transaction.html'
  model = Transactions
  form_class = TransactionsForm
  success_url='/transactions_list'