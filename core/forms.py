from django import forms
from data.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username','email','password','cpassword')

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}), max_length=50,required=True,help_text="Required")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}),max_length=100,required=True,help_text="Required. Provide a valid email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}),max_length=150,required=True)
    cpassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),max_length=150,required=True)

class LoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ('username','password')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Username',
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Password',
        'class':'w-full py-4 px-6 rounded-xl'
    }))