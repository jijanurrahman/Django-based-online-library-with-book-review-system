from django.contrib import admin
from .models import Category, Book, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_at', 'average_rating', 'total_reviews']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'author']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'category', 'description')
        }),
        ('Media', {
            'fields': ('cover_image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['book__title', 'user__username', 'comment']
    readonly_fields = ['created_at', 'updated_at']