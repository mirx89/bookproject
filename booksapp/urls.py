from django.urls import path
from . import views

app_name = 'booksapp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),  # Home View
    path('country_list/', views.CountryListView.as_view(), name='country_list'),  # Country List View
    path('country_form/', views.CountryCreateView.as_view(), name='country_create'),  # Country Form
    path('country_update/<int:pk>', views.CountryUpdateView.as_view(), name='country_update'),  # Country update
    path('country_delete/<int:pk>', views.CountryDeleteView.as_view(), name='country_delete'),  # Country delete

    path('language_list/', views.LanguageListView.as_view(), name='language_list'),  # Language List View
    path('language_create/', views.LanguageCreateView.as_view(), name='language_create'),  # Language Create form
    path('language_form_update/<int:pk> ', views.LanguageUpdateView.as_view(), name='language_form_update'),  # Language Update form
    path('language_delete/<int:pk> ', views.LanguageDeleteView.as_view(), name='language_delete'),  # Language delete form


    path('author_list/', views.AuthorListView.as_view(), name='author_list'),  # Author List View
    path('author_form/', views.AuthorCreateView.as_view(), name='author_form'),  # Author Create Form
    path('author_form_update/<int:pk>', views.AuthorUpdateView.as_view(), name='author_form_update'),  # Author Update Form
    path('author_detail/<int:pk>', views.AuthorDetailedView.as_view(), name='author_detail'),  # Author Detail view
    path('author_delete/<int:pk> ', views.AuthorDeleteView.as_view(), name='author_delete'),  # Author delete form


    path('book_list/', views.BookListView.as_view(), name='book_list'),  # Book List View
    path('book_form/', views.BookCreateView.as_view(), name='book_form'),  # Book List View
    path('book_form_update/<int:pk>', views.BookUpdateView.as_view(), name='book_form_update'),  # Book Update Form
    path('book_detail/<int:pk>', views.BookDetailedView.as_view(), name='book_detail'),  # Book Detail view
    path('book_delete/<int:pk> ', views.BookDeleteView.as_view(), name='book_delete'),  # Author delete form

]
