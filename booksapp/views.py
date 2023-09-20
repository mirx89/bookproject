from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import *  # All created forms
from .models import *  # All created models
# Create your views here.


class WriterRequiredMixin(UserPassesTestMixin):
    """Test: user in group Writer"""
    def test_func(self):
        return self.request.user.groups.filter(name="Writer").exists()


class EditorRequiredMixin(UserPassesTestMixin):
    """Test: user in group Editor"""
    def test_func(self):
        return self.request.user.groups.filter(name="Editor").exists()


class HomeView(TemplateView):
    template_name = 'booksapp/index.html'


class CountryListView(ListView):
    template_name = 'booksapp/country_list.html'
    model = Country
    # order result by country field name
    queryset = Country.objects.order_by('country')
    context_object_name = 'countries'  # object_list is default


class LanguageListView(ListView):
    # template language_list.html context_object_name is object_list
    model = Language
    queryset = Language.objects.order_by('language')


class AuthorListView(ListView):
    model = Author


class BookListView(ListView):
    model = Book


class CountryCreateView(CreateView):
    model = Country
    fields = '__all__'  # All fields from model
    success_url = reverse_lazy('booksapp:country_list')


class LanguageCreateView(WriterRequiredMixin, CreateView):
    model = Language
    form_class = LanguageCreateForm
    success_url = reverse_lazy('booksapp:language_list')


class AuthorCreateView(WriterRequiredMixin, CreateView):
    model = Author
    form_class = AuthorCreateForm
    success_url = reverse_lazy('booksapp:author_list')


class BookCreateView(WriterRequiredMixin, CreateView):
    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy('booksapp:book_list')


class CountryUpdateView(WriterRequiredMixin, UpdateView):
    template_name = 'booksapp/country_form_update.html'
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('booksapp:country_list')

    def form_valid(self, form):
        # Create additional checks
        return super().form_valid(form)


class LanguageUpdateView(WriterRequiredMixin, UpdateView):
    template_name = 'booksapp/country_form_update.html'
    model = Language
    form_class = LanguageCreateForm
    success_url = reverse_lazy('booksapp:language_list')

    def form_valid(self, form):
        # Create additional checks
        return super().form_valid(form)


class AuthorUpdateView(WriterRequiredMixin, UpdateView):
    template_name = 'booksapp/author_form_update.html'
    model = Author
    form_class = AuthorCreateForm
    success_url = reverse_lazy('booksapp:author_list')

    def form_valid(self, form):
        # Create additional checks
        return super().form_valid(form)


class BookUpdateView(WriterRequiredMixin, UpdateView):
    template_name = 'booksapp/book_form_update.html'
    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy('booksapp:book_list')

    def form_valid(self, form):
        # Create additional checks
        return super().form_valid(form)


class AuthorDetailedView(DetailView):
    # Default template model_detail.html => author_detail.html
    model = Author


class BookDetailedView(DetailView):
    model = Book


class CountryDeleteView(EditorRequiredMixin, DeleteView):
    # model_confirm_delete.html => country_confirm_delete.html
    model = Country
    success_url = reverse_lazy("booksapp:country_list")


class LanguageDeleteView(EditorRequiredMixin , DeleteView):
    model = Language
    success_url = reverse_lazy("booksapp:language_list")


class AuthorDeleteView(EditorRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy("booksapp:author_list")


class BookDeleteView(EditorRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("booksapp:book_list")


def custom403(request, exception):  # exception is not in use, can be only one letter as well
    return render(request, "403.html", status=403)


def custom404(request, exception):  # exception is not in use, can be only one letter as well
    return render(request, "404.html", status=404)