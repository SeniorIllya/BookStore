from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=200, help_text='Enter a genre of book')

    def __str__(self):
        return self.genre

class Language(models.Model):
    language = models.CharField(max_length=30, help_text="Enter language of this book")

    def __str__(self):
        return self.language
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter description of the book")
    isbn = models.CharField('ISBN', max_length=13, help_text='Enter uniqual code of book')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ManyToManyField(Language, help_text="Select a language for this book")
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        return ', '.join([ genre.genre for genre in self.genre.all()[:3]])
    display_genre.short_desription = 'Genre'
    
    def display_language(self):
        return ', '.join([ language.language for language in self.language.all()[:3]])
    display_language.short_description = 'Language'
    

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole store")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = [
        ('a', 'Available'),
        ('o', 'On sale soon'),
        ('u', 'Unavailable')
    ]
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True,
                              default='o', help_text='Book availability')
    sales_date = models.DateField('Set the sales start date(If the book is expected)', null=True,blank=True)
    #question
    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    short_biography = models.TextField(max_length=1000,null=True, help_text='Enter a short biography about this author')
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)
    
   # def genre_all(self):
    #    return ','.join([book.title])
    
    
