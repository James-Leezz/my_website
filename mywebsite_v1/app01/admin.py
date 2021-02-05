from django.contrib import admin
from app01.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    '''模型管理类 '''
    list_display=['username','password']
    list_per_page = 10

admin.site.register(User,UserAdmin)