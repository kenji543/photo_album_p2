from django.contrib import admin

from .models import Album, ContactMessage, Photo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'description', 'owner__username')
    list_filter = ('owner',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'uploaded_by', 'created_at')
    search_fields = ('title', 'description', 'album__title', 'uploaded_by__username')
    list_filter = ('album', 'uploaded_by')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at')
    search_fields = ('subject', 'name', 'email', 'message')
    readonly_fields = ('created_at',)
