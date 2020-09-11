from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import ( ListView,
                                   DetailView,
                                   CreateView,
                                   UpdateView, 
                                   DeleteView)
from django.contrib import messages
from .models import Post, Transaction
from .forms import AuthForm
from django.contrib.auth.decorators import login_required

class PostListView(ListView):
    model = Post
    template_name = 'market/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    permission_required = 'market.add_post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'market/about.html', {'title': 'About'})


class TransactionListView(LoginRequiredMixin, ListView):
    queryset = Transaction.objects.filter(authorised=True)
    context_object_name = 'transactions'
    ordering = ['-date']
    paginate_by = 100

class PendingTransactionListView(LoginRequiredMixin, ListView):
    template_name = 'market/pending.html'
    queryset = Transaction.objects.filter(authorised=False)
    context_object_name = 'transactions'
    ordering = ['date']
    paginate_by = 100

class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction

class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ['direction', 'value', 'recipient', 'description', 'details']

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

class TransactionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Transaction
    fields = ['direction', 'value', 'recipient', 'details', 'authorised']
    permission_required = 'market.change_transaction'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)