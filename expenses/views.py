from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Transactions, Category
from .forms import TransactionsForm, CategoryForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class HomeView(TemplateView):
    template_name = "expenses/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["transactions"] = Transactions.objects.all()
        transactions = Transactions.objects.filter(user=request.user)
        balance = 0
        for transaction in transactions:
            if transaction.status == 'C':
                if transaction.account == 'R':
                    balance += transaction.sum
                if transaction.account == 'S':
                    balance -= transaction.sum
        return context


class TransactionsView(ListView):
    template_name = "expenses/transaction/transactions_list.html"

    def get_queryset(self):
        queryset = Transactions.objects.filter(user=self.request.user)

        # self.show_all = self.request.GET.get("show_all") == "true"
        category = self.request.GET.get("category", "")
        status = self.request.GET.get("status", "")

        if category:
            queryset = queryset.filter(category_id=category)

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["statuses"] = Transactions.statuses
        context["statusSelected"] = self.request.GET.get("status", "")
        context["categorySelected"] = self.request.GET.get("category", "")

        return context


class CreateTransactionView(CreateView):
    template_name = "expenses/transaction/create_transaction.html"
    model = Transactions
    form_class = TransactionsForm
    success_url = reverse_lazy("transactions_list")

    def form_valid(self, form):
        form.instance.user = self.request.user  # привязка к текущему пользователю
        return super().form_valid(form)


class UpdateTransactionView(UpdateView):
    template_name = "expenses/transaction/update_transaction.html"
    model = Transactions
    form_class = TransactionsForm
    success_url = reverse_lazy("transactions_list")


class DeleteTransactionView(DeleteView):
    template_name = "expenses/transaction/delete_transaction.html"
    model = Transactions
    form_class = TransactionsForm
    success_url = reverse_lazy("transactions_list")


class ProfileView(TemplateView):
    template_name = "expenses/profile/profile.html"


class CategoryListView(ListView):
    template_name = "expenses/profile/categories/categories.html"
    model = Category
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryCreateView(CreateView):
    template_name = "expenses/profile/categories/create.html"
    model = Category
    success_url = reverse_lazy("categories")
    form_class = CategoryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    template_name = "expenses/profile/categories/update.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy("categories")

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryDeleteView(DeleteView):
    template_name = "expenses/profile/categories/delete.html"
    model = Category
    success_url = reverse_lazy("categories")

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
