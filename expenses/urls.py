from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "transactions_list/", views.TransactionsView.as_view(), name="transactions_list"
    ),
    path(
        "transactions/create/",
        views.CreateTransactionView.as_view(),
        name="create_transaction",
    ),
    path(
        "transactions/<pk>/update/",
        views.UpdateTransactionView.as_view(),
        name="update_transaction",
    ),
    path(
        "transactions/<pk>/delete/",
        views.DeleteTransactionView.as_view(),
        name="delete_transaction",
    ),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("profile/categories", views.CategoryListView.as_view(), name="categories"),
    path(
        "profile/categories/create",
        views.CategoryCreateView.as_view(),
        name="create_categories",
    ),
    path(
        "profile/categories/<pk>/delete",
        views.CategoryDeleteView.as_view(),
        name="delete_categories",
    ),
    path(
        "profile/categories/<pk>/update",
        views.CategoryUpdateView.as_view(),
        name="update_categories",
    ),
]
