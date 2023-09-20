import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import (MinLengthValidator, MinValueValidator, MaxValueValidator)


# Create your models here.
class Country(models.Model):
    # Country name with max length 50, min length 3 letter
    country = models.CharField(max_length=50, validators=[MinLengthValidator(2)])

    class Meta:
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.country


class Language(models.Model):
    language = models.CharField(max_length=50, validators=[MinLengthValidator(3)])

    def __str__(self):
        return self.language


class Author(models.Model):
    firstname = models.CharField(max_length=25, validators=[MinLengthValidator(2)])
    lastname = models.CharField(max_length=25, validators=[MinLengthValidator(2)])
    birth = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    class Meta:
        #  Default order lastname and then firstname
        ordering = ['lastname', 'firstname']

    def fullname(self):
        """Show fullname of the author"""
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        """ Default ADMIN page view"""
        return f'{self.fullname()}, {self.birth}, {self.country}'


def validate_digits_length(isbn):
    """Check ISBN number digits"""
    if not (isbn.isdigit() and len(isbn) == 13):
        raise ValidationError('The ISBN number must be 13 digits long and no letters.')


def max_value_current_year(year):
    """Return current year"""
    return MaxValueValidator(datetime.date.today().year)(year)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    book_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(verbose_name='ISBN number', max_length=13, validators=[validate_digits_length])
    numbers_of_page = models.PositiveIntegerField(validators=[MinValueValidator(2)])
    description = models.TextField(null=True, blank=True)
    book_published_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), max_value_current_year])

    class Meta:
        """ Default result ordering """
        ordering = ['title']

    def book_info(self):
        """ Show simple book info"""
        return f'{self.title}, {self.author.fullname()}'

    def __str__(self):
        """ Admin page show info"""
        return (f'{self.title}, {self.author}, {self.book_language}, {self.isbn}, {self.numbers_of_page}, '
                f'{self.book_published_year}, {self.description[:25]}')
