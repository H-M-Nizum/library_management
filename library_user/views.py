from django.shortcuts import render, redirect, get_object_or_404
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
from django.contrib.auth.models import User

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
from .models import BorrowedBookModel

# Create your views here.

class profileview1(TemplateView):
    template_name = 'profile.html'

def profileview(request):
    data = BorrowedBookModel.objects.filter(user=request.user)
    print(data)
    print(request.user)
    return render(request, 'profile.html', {'data':data})

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
    
    
# def Borrowed_Book1(request, id):
#     book = BookModel.objects.get(pk=id)

#     user_balance = int(request.user.account.balance)
#     borrowing_price = int(book.borrowing_price)
#     if user_balance >= borrowing_price:
#         print('borrowed book')
#         print(request.user)
#         print(book)
#         # BorrowedBook.objects.create(user=request.user, book=book)
        
#     else:
#         print('your amount is low, can not borrowed this book')
    
#     return redirect(reverse("book_details", args=[book.id]))




def Borrowed_Book(request, id):
    book = get_object_or_404(BookModel, pk=id)

    user_balance = int(request.user.account.balance)
    borrowing_price = int(book.borrowing_price)

    if user_balance >= borrowing_price:
        # # Create and save BorrowedBook instance
        BorrowedBookModel.objects.create(user=request.user, book=book)
        
    
        request.user.account.balance -= borrowing_price
        request.user.account.save()

        print(request.user.account.account_no)
        print(request.user)

        print(book)
    else:
        print('Your amount is low, cannot borrow this book')

    return redirect(reverse("book_details", args=[book.id]))



def Return_book(request, id):
    record = BorrowedBookModel.objects.get(pk=id)
    print(record.book.borrowing_price)

    
    request.user.account.balance += int(record.book.borrowing_price)
    request.user.account.save()

    
    record.delete()
    return redirect('profile')