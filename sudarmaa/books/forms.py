from django import forms
from books.models import Book, Page, Shelf, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'category', 'photo', 'description', 'authors', 'language')
        exclude = ('creator', 'status')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 15, 'class':'span6'}),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ('user',)
        widgets = {
            'biography': forms.Textarea(attrs={'rows': 15, 'class':'span6'}),
        }

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 25, 'class':'span14'}),
            'title': forms.TextInput(attrs={'class': 'span6'})
        }

class ShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        exclude = ('is_public', 'books')

