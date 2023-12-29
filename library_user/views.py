from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from .forms import DepositForm, CommentForm
# Create your views here.
from django.views.generic import TemplateView
# Create your views here.
from django.urls import reverse

class UserRegistrationViews(FormView):
    template_name = 'user_regostration.html'
    form_class = RegisterForm
    success_url =reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid functions call hobe jodi sob thik thake


class Userloginviews(LoginView):
    template_name = 'user_login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
class userlogoutview(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    
def deposit_money(request):
    user_account = request.user.account  
    
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user_account.balance += amount
            user_account.save()
            return redirect('home')  
    else:
        form = DepositForm()

    return render(request, 'deposit_money.html', {'form': form})

    
from library.models import BookModel, Category

# Create your views here.

class profileview(TemplateView):
    template_name = 'profile.html'

def seeBookview(request, category_slug = None):
    data = BookModel.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = BookModel.objects.filter(category = category)
        
    categories = Category.objects.all()
    return render(request, 'seeBook.html', {'data':data, 'category': categories})




class BookDetailsView(DetailView):
    model = BookModel
    # pk_url_kwarg = 'id'
    template_name = 'Book_details.html'
    
    
def BorrowedBook(request, id):
    book = BookModel.objects.get(pk=id)
    user_balance = int(request.user.account.balance)
    borrowing_price = int(book.borrowing_price)
    if user_balance >= borrowing_price:
        print('borrowed book')
        
    else:
        print('your amount is low, can not borrowed this book')
    
    return redirect(reverse("book_details", args=[book.id]))