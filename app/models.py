import datetime

from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.category}'


class Product(models.Model):
    Size = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )
    Availability = (('Còn Hàng', 'Còn Hàng'), ('Hết Hàng', 'Hết Hàng'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, default='')
    image = models.ImageField(upload_to='ecommerce/pimg')
    name = models.CharField(max_length=150, default="")
    brand = models.CharField(max_length=255,default="")
    description = models.TextField(default="")
    Size = models.CharField(choices=Size, null=True, max_length=100)
    price = models.IntegerField(default=0)
    Availability = models.CharField(choices=Availability,null=True,max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class Reviews(models.Model):
    Rate = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),)
    # user = models.ForeignKey(User,on_delete=models.PROTECT)
    product_re = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()
    rate = models.CharField(choices = Rate, null=True,max_length=100)
    
    def __str__(self):
        return f'{self.product_re} - {self.name} '
    

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'exists': 'Email đã tồn tại.'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mật Khẩu'
        self.fields['password2'].widget.attrs['placeholder'] = 'Nhập Lại Mật Khẩu'

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user
    
    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user    

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']


class Contact_us(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Order(models.Model):
    image = models.ImageField(upload_to='ecommerce/order/image')
    product = models.CharField(max_length=1000, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=5)
    price = models.IntegerField()
    total = models.CharField(max_length=1000, default='')
    address = models.TextField()
    phone = models.CharField(max_length=12)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.product
