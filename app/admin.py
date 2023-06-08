from django.contrib import admin
from .models import ProfileData, Posts, SocialLinks, BaseModel, About

# Register your models here.


@admin.register(ProfileData)
class ProfileDataAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", "description")
    ordering = ("created_at", )


@admin.register(SocialLinks)
class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", "icon")
    ordering = ("order", )


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("title", )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("title", )





