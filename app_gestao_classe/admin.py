from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_gestao_classe.models import UsuarioCustomizado
# Register your models here.

class UserModel(UserAdmin):
    pass

admin.site.register(UsuarioCustomizado, UserModel)
