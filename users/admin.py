from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerUserCreationForm, CustomerUserChangeForm
from .models import CustomerUser


# Register your models here.
class CustomerUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomerUserChangeForm
    model = CustomerUser
    list_display = ['email', 'username', 'age', 'is_staff']


admin.site.register(CustomerUser, CustomerUserAdmin)
