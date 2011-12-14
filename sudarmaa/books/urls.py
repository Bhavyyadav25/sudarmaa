from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required, permission_required
from books.views import (HomeView, MyBooksView, BooksInCategory, BookDetail,
    CreateBook, ShowMyBook, EditPage, EditPageContent, PagePreview, 
    BookTOC, ReadPage, ShelfView, ShelfList, ShelfCreate, AddRating,
    PublishBook, BookShelfAction, BookmarkAdd, BookmarkRemove, BookmarksView,
    StaffPicks, LatestBooks, CreateAuthor, AuthorView, DownloadPage, DownloadBook,
    UpdateBook)

# general use case
urlpatterns = patterns("",
    url(r"^$", HomeView.as_view(template_name="books/home.html"), 
    name="home"),
    url(r"^books/$", BooksInCategory.as_view(template_name='books/books_with_category.html',), 
    name="books-in-category"),
    url(r"^books/staff-pick/$", StaffPicks.as_view(template_name='books/books_with_category.html',), 
    name="staff-picks"),
    url(r"^books/latest/$", LatestBooks.as_view(template_name='books/books_with_category.html',), 
    name="latest-books"),
    url(r"^author/(?P<pk>\d+)/$", AuthorView.as_view(), 
    name="author-show"),
)

# for publishers
urlpatterns += patterns("",
    url(r"^publisher/book/publish/$", permission_required('books.add_book')(PublishBook.as_view()), 
    name="publish-book"),
    url(r"^publisher/book/$", permission_required('books.add_book')(MyBooksView.as_view()), 
    name="published-books"),
    url(r"^publisher/book/create/$", permission_required('books.add_book')(CreateBook.as_view()), 
    name="create-book"),
    url(r"^publisher/book/update/(?P<pk>\d+)/$", permission_required('books.add_book')(UpdateBook.as_view()), 
    name="update-book"),
    url(r"^publisher/book/edit/(?P<pk>\d+)/$", permission_required('books.add_book')(ShowMyBook.as_view()), 
    name="my-books-show"),
    url(r"^publisher/page/preview/$", permission_required('books.add_book')(PagePreview.as_view()), 
    name="page-preview"),
    url(r"^publisher/page/edit/$", permission_required('books.add_book')(EditPage.as_view()), 
    name="edit-page"),
    url(r"^publisher/page/edit/(?P<pk>\d+)/$", permission_required('books.add_book')(EditPageContent.as_view()), 
    name="edit-page-content"),
    url(r"^publisher/author/create/$", permission_required('books.add_book')(CreateAuthor.as_view()), 
    name="create-author"),
)

# maintaining shelf
urlpatterns += patterns("",
    url(r"^shelf/(?P<pk>\d+)/$", login_required(ShelfView.as_view()),
    name="shelf-detail"),
    url(r"^shelf/$", login_required(ShelfList.as_view()),
    name="shelf-index"),
    url(r"^shelf/create/$", login_required(ShelfCreate.as_view()),
    name="shelf-create"),
    url(r"^shelf/add/book/$", login_required(BookShelfAction.as_view()),
    name="shelf-action"),
)

# reading through books, rating etc...
urlpatterns += patterns("", 
    url(r"^book/(?P<pk>\d+)/$", BookDetail.as_view(),
    name="book-detail"),
    url(r"^book/(?P<pk>\d+)/toc/$", login_required(BookTOC.as_view()),
    name="book-toc"),
    url(r"^book/(?P<pk>\d+)/read/$", login_required(ReadPage.as_view()),
    name="read-page"),
    url(r"^book/(?P<object_id>\d+)/rate/(?P<score>\d+)/$", AddRating.as_view(), 
    name="book-rate"),
)

# bookmarking
urlpatterns += patterns("",
    url(r"^bookmark/add/(?P<page_id>\d+)/", login_required(BookmarkAdd.as_view()), 
    name='bookmark-add'),
    url(r"^bookmark/remove/(?P<page_id>\d+)/", login_required(BookmarkRemove.as_view()),
    name='bookmark-remove'),
    url(r"^bookmark/", login_required(BookmarksView.as_view()),
    name='bookmark-index'),
)

# downloading
urlpatterns += patterns("",
    url(r"download/(?P<pk>\d+)/$", login_required(DownloadPage.as_view()),
    name='download-page'),
    url(r"download/book/(?P<pk>\d+)/$", login_required(DownloadBook.as_view()),
    name='download-book'),
)
