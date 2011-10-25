# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from books.models import Book, Category, Pick
from books.forms import BookForm

class HomeView(TemplateView):
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'new_books' : Book.objects.all()[:4],
            'picked_books': Book.objects.filter(
                pick__isnull=False).order_by('pick__order_number')[:4],
            'categories' : Category.objects.all()
        })
        return context

class MyBooksView(ListView):
    context_object_name = 'my_books'
    paginate_by = 10

    def get_queryset(self):
        return self.request.user.book_set.all()

class BooksInCategory(ListView):
    context_object_name = 'books'
    paginate_by = 3

    def get_queryset(self):
        category_id = self.request.GET.get('cat', None)
        if category_id:
            query_set = Book.objects.filter(category__id=category_id)
        else:
            query_set = Book.objects.all()
        return query_set

    def get_context_data(self, **kwargs):
        context = super(BooksInCategory, self).get_context_data(**kwargs)
        context.update({
            'categories' : Category.objects.all()
        })
        category_id = self.request.GET.get('cat', None)
        if category_id: context.update({ 'cat' : category_id })
        return context

class CreateBook(CreateView):
    template_name = 'books/book_form.html'
    form_class = BookForm

    def get_success_url(self):
        book = self.object
        book.creator = self.request.user
        book.save()
        return reverse('my-books-show', kwargs={'pk':book.id})

class ShowMyBook(DetailView):
    context_object_name = 'book'
    template_name = 'books/my_book.html'

    def get_queryset(self):
        return Book.objects.filter(creator=self.request.user)

