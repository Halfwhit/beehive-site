from django.urls import path
from .views import (
    PostListView,
    TransactionListView,
    PostDetailView,
    TransactionDetailView,
    PendingTransactionListView,
    PostCreateView,
    PostUpdateView,
    TransactionCreateView,
    TransactionUpdateView,
    PostDeleteView
)
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', PostListView.as_view(), name='market-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='market-about'),
    path('transactions/', TransactionListView.as_view(), name='market-transactions'),
    path('transaction/new/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('pending/', login_required(PendingTransactionListView.as_view()), name='market-pending')
]