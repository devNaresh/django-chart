from django.contrib import admin
from .models import User,VideoData,WatchedVideo
# Register your models here.

class WatchedVideoInline(admin.TabularInline):
    model = WatchedVideo
    extra = 0
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    inlines = [WatchedVideoInline]
    
admin.site.register(User,UserAdmin)
admin.site.register(VideoData)