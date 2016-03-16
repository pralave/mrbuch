from django.contrib import admin
from .forms import RegistrationForm
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["__unicode__",]
    form = RegistrationForm
admin.site.register(User,UserAdmin)
