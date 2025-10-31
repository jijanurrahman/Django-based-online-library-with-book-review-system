from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from .models import Book, Review, Category
from .forms import UserRegisterForm, ReviewForm, BookSearchForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.username}!')
            return redirect('book_list')
    else:
        form = UserRegisterForm()
    return render(request, 'books/register.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    form = BookSearchForm(request.GET)
    
    # Search functionality
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    
    if category_id:
        books = books.filter(category_id=category_id)
    
    context = {
        'books': books,
        'form': form,
        'query': query,
    }
    return render(request, 'books/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    user_review = None
    
    if request.user.is_authenticated:
        try:
            user_review = Review.objects.get(book=book, user=request.user)
        except Review.DoesNotExist:
            user_review = None
    
    context = {
        'book': book,
        'reviews': reviews,
        'user_review': user_review,
    }
    return render(request, 'books/book_detail.html', context)


@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    # Check if user already reviewed this book
    if Review.objects.filter(book=book, user=request.user).exists():
        messages.warning(request, 'You have already reviewed this book!')
        return redirect('book_detail', pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added successfully!')
            return redirect('book_detail', pk=pk)
    else:
        form = ReviewForm()
    
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'books/add_review.html', context)


@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated successfully!')
            return redirect('book_detail', pk=review.book.pk)
    else:
        form = ReviewForm(instance=review)
    
    context = {
        'form': form,
        'book': review.book,
        'review': review,
    }
    return render(request, 'books/edit_review.html', context)


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    book_pk = review.book.pk
    
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted successfully!')
        return redirect('book_detail', pk=book_pk)
    
    context = {
        'review': review,
    }
    return render(request, 'books/delete_review.html', context)