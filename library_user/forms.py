# django builtin model forom
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserAccountModel, Comment

class RegisterForm(UserCreationForm):
    
    # If i want to any fields custom modify
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))
    
    class Meta:
        model = User
        
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def save(self, commit= True):
        user =  super().save(commit=False)
        if commit == True:
            user.save() # user model a data save hobe
            
            
            
            
            # UserBankAccountModel model a data save hobe
            UserAccountModel.objects.create(
                user = user,
                account_no = 1000000 + user.id
            )
            
            
        return user
        

class DepositForm(forms.Form):
    amount = forms.DecimalField(label='Amount', max_digits=12, decimal_places=2)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']