from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Transactions, Category
from .forms import TransactionsForm, CategoryForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HomeView(TemplateView):
    template_name = "expenses/pages/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["transactions"] = Transactions.objects.all()
        return context


class TransactionsView(ListView):
    template_name = 'expenses/transaction_management/transactions_list.html'
    model = Transactions

    def get_queryset(self):
        self.show_all = self.request.GET.get("show_all") == "true"
        if self.show_all:
            return Transactions.objects.all()
        else:
            return Transactions.objects.filter(status="completed")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["show_all"] = self.show_all
        return context


class CreateTransactionView(CreateView):
    template_name = 'expenses/transaction_management/create_transaction.html'
    model = Transactions
    fields = "__all__"
    success_url = reverse_lazy('transactions_list')


class UpdateTransactionView(UpdateView):
    template_name = 'expenses/transaction_management/update_transaction.html'
    model = Transactions
    form_class = TransactionsForm
    fields = "__all__"
    success_url = reverse_lazy('transactions_list')


class DeleteTransactionView(DeleteView):
    template_name = 'expenses/transaction_management/delete_transaction.html'
    model = Transactions
    form_class = TransactionsForm
    success_url = "/transactions_list"
    fields = "__all__"
    success_url = reverse_lazy('transactions_list')
