from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('transactions_list/', views.TransactionsView.as_view(), name='transactions_list'),
    path('transactions/create/', views.CreateTransactionView.as_view(), name='create_transaction'),
    path('transactions/<pk>/update/', views.UpdateTransactionView.as_view(), name='update_transaction'),
    path('transactions/<pk>/delete/', views.DeleteTransactionView.as_view(), name='delete_transaction'),
]
